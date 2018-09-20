from django.shortcuts import render
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize
import json

# Create your views here.

def main_view(request):
	return render(request,'fndApp/main_view.html',{})

def result(request):
	mainTile=request.POST.get('title')
	stopWords=set(stopwords.words('english')) 
	word_tokens = word_tokenize(mainTile) 
	words=[w for w in word_tokens if w not in stopWords]
	wordsJson=json.dumps(words)
	return render(request,'fndApp/result.html',{'title':wordsJson})