import os
import environ
from pathlib import Path

# 環境変数を管理するためのenvオブジェクト作成
env = environ.Env()
# .envファイルの読み込み
env.read_env('.env')
# .envファイルからSECRET_KEYを読み込み
SECRET_KEY = env('SECRET_KEY')
# .envファイルからDEBUGの値を取得し、真偽値に変換
DEBUG = env.bool('DEBUG', default=False)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

DATABASES = {
    'default': {
        'ENGINE': env('DATABASE_ENGINE', default='django.db.backends.sqlite3'),
        'NAME': env('DATABASE_DB', default=os.path.join(BASE_DIR, 'db.sqlite3')),
        # MySQLやPostgreSQLを使用する場合は、以下の設定を使用
        'USER': env('DATABASE_USER', default=''),
        'PASSWORD': env('DATABASE_PASSWORD', default=''),
        'HOST': env('DATABASE_HOST', default=''),
        'PORT': env('DATABASE_PORT', default=''),
    }
}

# ALLOWED_HOSTSを環境変数から取得、デフォルトはlocalhost
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['localhost', '127.0.0.1'])
