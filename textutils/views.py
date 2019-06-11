# I have created this file - himanshu
from django.http import HttpResponse
from django.shortcuts import render

def indexbootstrap(request):
	return render(request, 'indexbootstrap.html')

def analyzebootstrap(request):
	djtext = request.POST.get('text', 'default')

	removepunc = request.POST.get('removepunc', 'off')
	caps = request.POST.get('caps', 'off')
	sremove = request.POST.get('sremove', 'off')
	nlremove = request.POST.get('nlremove', 'off')


	punctuation = '''!"#$%&'()*+,-./:;?@[\]^_`{|}~'''
	if removepunc == 'on':
		analyzed = ""
		for char in djtext:
			if char not in punctuation:
				analyzed = analyzed + char
		purpose = "Removed"			
	else:
		analyzed = djtext	
		purpose = "Not Removed"		



	if caps == 'on':
		analyzed = ""
		for char in djtext:
			analyzed = analyzed + char.upper()
		purpose = "Capitalized"
	else:
		analyzed = djtext
		purpose = "Not Capitalized"



	if sremove == "on": 
		analyzed = ""
		for index , char in enumerate(djtext):
			if not (djtext[index] == " " and djtext[index+1] == " "):
				analyzed =	analyzed + char



	if nlremove == "on":
		analyzed = ""
		for char in djtext:
			if char != "/n":
				analyzed = analyzed + char

	params = { 'purpose':purpose,'analyzed_text':analyzed,}
	return render(request, 'analyzebootstrap.html', params)

