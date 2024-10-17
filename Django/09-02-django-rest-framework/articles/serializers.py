from rest_framework import serializers
from .models import Article,Comment


class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = (
            'id',
            'title',
            'content',
        )


class ArticleSerializer(serializers.ModelSerializer):
    class CommentDetailSerializer(serializers.ModelSerializer):
        class Meta:
            model = Comment
            fields = ('id', 'content',)
    
    # comment_set 역함수 테이블을 오버라이드
    comment_set = CommentDetailSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)

    class Meta:
        model = Article
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class ArticleTitleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Article
            fields = ('title',)
    
    # 기존 article 데이터 값을 override
    # 필드를 override 하게 되면 Meta클래스의 read_only_fields를 사용할 수 없음
    # 모델 시리얼라이저의 read_only 인자 값으로 재설정
    article = ArticleTitleSerializer(read_only = True)
    
    class Meta:
        model = Comment
        fields = '__all__'
        # fields에 작성된 필드는 모두 유효성 검사에 포함됨
        # 1. 외래 키 데이터는 유효성 검사에서는 제외
        # 2. 결과 데이터에는 포함하고 싶음
        # -> 읽기 전용 필드 지정
        # 외래 키 필드를 읽기 전용 필드로 지정
        # read_only_fields = ('article',)