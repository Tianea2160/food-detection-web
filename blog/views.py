from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Photo, Output
import cheak
import test
# Create your views here.


def post_list(request):
    posts = Post.objects.order_by('-pk')
    content ={'posts': posts}
    return render(request, 'post_list.html', content)

def create(request):
    if(request.method == 'POST'):
        post = Post()
        post.title = request.POST['title']
        post.save()
        # name 속성이 imgs인 input 태그로부터 받은 파일들을 반복문을 통해 하나씩 가져온다
        for img in request.FILES.getlist('image'):
            # Photo 객체를 하나 생성한다.
            photo = Photo()
            # 외래키로 현재 생성한 Post의 기본키를 참조한다.
            photo.post = post
            # imgs로부터 가져온 이미지 파일 하나를 저장한다.
            photo.image = img
            # 데이터베이스에 저장
            photo.save()
            result_file = "C:\\Users\\ipsl\\Desktop\\darknet-master\\darknet-master\\build\\darknet\\x64\\result.txt"


            # 이미지 예측값 알아내기
            cheak.image_predeict(photo.image.url)
            test.pretreatment_file(result_file)
            with open("p_result.txt", 'r') as f:
                for line in f.readlines():
                    output = Output()
                    output.post = post
                    output.name = line
                    output.save()
        return redirect('/blog/')
    else:
        return render(request, 'post_create.html')


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    content = {'post': post}
    return render(request, 'post_detail.html', content)
