from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from clothing_recommend.forms import RecommendForm

# Create your views here.
@login_required
def recommend_view(request):
	context = {}
	style1 = ['优雅','百搭','通勤']
	style2 = ['甜美']
	style3 = ['街头']
	style = ','.join(style1) +','+ ','.join(style2) +','+ ','.join(style3)
	popular1 = ['不对称','交叉带','亮丝','亮闪闪面料','做旧','拉链','破洞','纱网','纽扣','绣花','荷叶边','蝴蝶结','镂空','领口结绳设计']
	popular2 = ['刺绣','水洗']
	popular3 = ['印花','拼接']
	popular4 = ['口袋','蕾丝']
	popular = ','.join(popular1)+','+','.join(popular2)+','+','.join(popular3)+','+','.join(popular4)
	pattern1 = ['空','字母拼接','字母拼色','拼接','碎花']
	pattern2 = ['人物','纯色']
	pattern3 = ['其他']
	pattern4 = ['字母','条纹','格子']
	pattern = ','.join(pattern1)+',' + ','.join(pattern2)+',' + ','.join(pattern3)+',' + ','.join(pattern4)
	if request.method == "POST":
		Recommend_form = RecommendForm(request.POST)
		if Recommend_form.is_valid():
			parameter = Recommend_form.cleaned_data
			if parameter['style'] in style1:
				context['A'] = 5.263
				context['B'] = 5.263
				context['C'] = 89.474
			elif parameter['style'] in style2:
				if parameter['popular'] in popular1:
					context['A'] = 0.000
					context['B'] = 0.000
					context['C'] = 0.000
				elif parameter['popular'] in popular2:
					context['A'] = 0.000
					context['B'] = 0.000
					context['C'] = 100.000
				elif parameter['popular'] in popular3:
					context['A'] = 0.000
					context['B'] = 75.000
					context['C'] = 25.000
				elif parameter['popular'] in popular4:
					context['A'] = 60.000
					context['B'] = 40.000
					context['C'] = 0.000
				else:
					return render(request, 'clothing_recommend/show.html', {"form": Recommend_form, 'status':
						'popular请输入：'+popular+' 中的一个元素'})
			elif parameter['style'] in style3:
				if parameter['pattern'] in pattern1:
					context['A'] = 0.000
					context['B'] = 0.000
					context['C'] = 0.000
				elif parameter['pattern'] in pattern2:
					context['A'] = 100.000
					context['B'] = 0.000
					context['C'] = 0.000
				elif parameter['pattern'] in pattern3:
					context['A'] = 0.000
					context['B'] = 0.000
					context['C'] = 100.000
				elif parameter['pattern'] in pattern4:
					context['A'] = 23.529
					context['B'] = 76.417
					context['C'] = 0.000
				else:
					return render(request, 'clothing_recommend/show.html', {"form": Recommend_form, 'status':
						'pattern请输入：' + pattern + ' 中的一个元素'})
			else:
				return render(request, 'clothing_recommend/show.html', {"form": Recommend_form, 'status':
					'style请输入：' + style + ' 中的一个元素'})
			context['form'] = Recommend_form
			return render(request, 'clothing_recommend/show.html', context )
		else:
			return render(request, 'clothing_recommend/show.html', {"form": Recommend_form, 'status': '输入不合法'})
	elif request.method == "GET":
		Recommend_form = RecommendForm()
		return render(request, 'clothing_recommend/show.html', {"form": Recommend_form})
	else:
		Recommend_form = RecommendForm()