import nmap,time,json
from unit_Tools.sqlData_unitTools import  sqlData_unitTools

sqlData_unitToolsC = sqlData_unitTools()

class nmap_unitTools(object):

    def __init__(self):
        self.nm = nmap.PortScanner()


    def nmap_scan(self,hosts,ports):
        print("-" * 15, "UnitTools nmap_scan - start", "-" * 15)
        try:
            self.nm.scan(hosts=hosts,ports=ports,arguments='-sS -Pn --open --min-parallelism 10 --host-timeout 10')
            print(self.nm.command_line())
            #print(self.nm.all_hosts())
            #print(self.nm.scaninfo())
            host_list = self.nm.all_hosts()
            result_hostList = []
            if host_list:
                hostList_info = [self.nm[host] for host in host_list]
                #print(hostList_info)
                # 循环主机列表，并对主机列表的nm格式进行信息提取
                for row in hostList_info:
                    host_ip  = (row.get("addresses")).get('ipv4')
                    name = (row.get('hostnames')[0]).get('name')
                    if not name:
                        name = "Null"
                    portState_dict = {}
                    if row.get('tcp',None):
                        # 获取TCP扫描端口列表，若存在则扫描，不存在直接存储IP和name即可
                        tcp_openPortlist = list(row.get('tcp').keys())
                        # 循环获取到的TCP端口，并取得其中的状态
                        for portNumber in tcp_openPortlist:
                            portState = ((row.get('tcp')).get(portNumber)).get('state')
                            if portState == "open":
                                portState_dict[portNumber] = portState
                        result_hostList.append([host_ip,name,portState_dict,time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())])
                    else:
                        result_hostList.append([host_ip,name,portState_dict,time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())])
                return {"code":"true","tip":"notNull","hostList_info":result_hostList}
            else:
                return {"code":"false","tip":"Null"}
        except BaseException as e:
            print("-" * 15, "UnitTools nmap_scan - BaseException:%s"%(e), "-" * 15)
            return {"code": "false", "tip": "BaseException"}

    def scanRe_insertDB(self,hosts,ports):
        print("-" * 15, "UnitTools scanRe_insertDB - start", "-" * 15)
        result = self.nmap_scan(hosts,ports)
        if result.get('code',None) == "false":
            print("-" * 15, "UnitTools scanRe_insertDB - resultCodeFalse", "-" * 15)
            return False
        else:
            sql = '''insert into nampscan values (%s,%s)'''
            for i in result.get("hostList_info"):
                r = sqlData_unitToolsC.excute(sql, [None, json.dumps(i)])
            if r == False:
                print("-" * 15, "UnitTools scanRe_insertDB - sqlExcuteFalse", "-" * 15)
                return False
        print("-" * 15, "UnitTools scanRe_insertDB - Goodend", "-" * 15)
        return True

if __name__ == "__main__":

    a = nmap_unitTools()

    # b = a.nmap_scan(hosts='192.168.31.0/24', ports='1-1110')
    # print(b.get("hostList_info"))
    # sql = '''insert into nampscan values (%s,%s)'''
    # for i in b.get("hostList_info"):
    #     sqlData_unitToolsC.excute(sql,[None,json.dumps(i)])
    sql = '''select nmapRow from nampscan'''
    search_nmapscan = sqlData_unitToolsC.search(sql, show=True)
    return_jsonList = []
    if search_nmapscan:
        for i in search_nmapscan:
            return_jsonList.append(i[0])
    print(return_jsonList)
