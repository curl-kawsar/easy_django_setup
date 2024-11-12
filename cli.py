# cli.py
import os
import click
import subprocess

@click.group()
def cli():
    """Easy Django Setup Tool by Kawsar"""
    pass

@click.command(help="Initialize a new Django project with various options.")
@click.argument('project_name')
def init(project_name):
    """Initialize a new Django project with various options."""
    # Fancy header
    click.echo(click.style("\n=====================================", fg='cyan', bold=True))
    click.echo(click.style("||                                 ||", fg='cyan', bold=True))
    click.echo(click.style("||      Easy Django Setup Tool     ||", fg='cyan', bold=True))
    click.echo(click.style("||           by Kawsar             ||", fg='cyan', bold=True))
    click.echo(click.style("||                                 ||", fg='cyan', bold=True))
    click.echo(click.style("=====================================\n", fg='cyan', bold=True))
    
    # Step 1: Take all options input
    jwt_auth = click.confirm(click.style('Do you want to include JWT authentication?', fg='green', bold=True))
    token_auth = click.confirm(click.style('Do you want to include token-based authentication?', fg='green', bold=True))
    google_login = click.confirm(click.style('Do you want to include Google login?', fg='green', bold=True))
    redis_setup = click.confirm(click.style('Do you want to include Redis setup?', fg='green', bold=True))
    docker_setup = click.confirm(click.style('Do you want to include Docker setup?', fg='green', bold=True))
    swagger_docs = click.confirm(click.style('Do you want to include Swagger documentation?', fg='green', bold=True))
    create_app = click.confirm(click.style('Do you want to create a new app?', fg='green', bold=True))
    
    # Step 2: Generate Django project
    subprocess.run(['django-admin', 'startproject', project_name])
    
    # Step 3: Create predefined configurations
    create_predefined_configs(project_name)
    
    # Step 4: Add options based on user input
    if jwt_auth:
        setup_jwt(project_name)
    if token_auth:
        setup_token_auth(project_name)
    if google_login:
        setup_google_login(project_name)
    if redis_setup:
        setup_redis(project_name)
    if docker_setup:
        setup_docker(project_name)
    if swagger_docs:
        setup_swagger(project_name)
    
    # Step 5: Integrate Cloudinary/AWS S3
    setup_file_uploads(project_name)
    
    # Step 6: Configure secure cookies
    configure_secure_cookies(project_name)
    
    # Step 7: Create a new app if requested
    if create_app:
        app_name = click.prompt(click.style('Enter the app name', fg='yellow', bold=True))
        create_new_app(project_name, app_name)
    
    # Step 8: Summary message
    click.echo(click.style(f"\nProject {project_name} setup complete. Follow the instructions below to get started:", fg='blue', bold=True))
    click.echo(click.style(f"1. Navigate to the project directory: cd {project_name}", fg='blue'))
    click.echo(click.style("2. Create a virtual environment and install dependencies.", fg='blue'))
    click.echo(click.style("3. Run the development server: python manage.py runserver\n", fg='blue'))

def create_predefined_configs(project_name):
    """Create predefined configuration files."""
    # Create .env.example
    with open(os.path.join(project_name, '.env.example'), 'w') as f:
        f.write("DEBUG=True\nSECRET_KEY=your_secret_key\n")
    
    # Create .gitignore
    with open(os.path.join(project_name, '.gitignore'), 'w') as f:
        f.write("*.pyc\n__pycache__/\n.env\n")
    
    # Create logging configuration
    with open(os.path.join(project_name, 'logging.conf'), 'w') as f:
        f.write("[loggers]\nkeys=root\n")
    
    # Create templates directory
    templates_dir = os.path.join(project_name, 'templates')
    os.makedirs(templates_dir, exist_ok=True)
    
    # Add templates directory to settings
    settings_path = os.path.join(project_name, project_name, 'settings.py')
    with open(settings_path, 'a') as f:
        f.write("\nimport os\n")
        f.write("\n# Templates Directory\n")
        f.write("TEMPLATES[0]['DIRS'] += [os.path.join(BASE_DIR, 'templates')]\n")
    
    # Create README.txt
    readme_path = os.path.join(os.path.dirname(__file__), 'README.txt')
    with open(readme_path, 'w') as f:
        f.write("Easy Django Setup Tool by Kawsar\n")
        f.write("=================================\n\n")
        f.write("This CLI tool helps you set up a new Django project with various options.\n\n")
        f.write("Usage:\n")
        f.write("------\n")
        f.write("1. Run the CLI tool with the project name as an argument:\n")
        f.write("   python cli.py init <project_name>\n\n")
        f.write("2. Follow the prompts to include various options such as JWT authentication, token-based authentication, Google login, Redis setup, Docker setup, Swagger documentation, and creating a new app.\n\n")
        f.write("3. The tool will generate the Django project and configure it based on your inputs.\n\n")
        f.write("4. Navigate to the project directory and follow the instructions to get started:\n")
        f.write("   cd <project_name>\n")
        f.write("   Create a virtual environment and install dependencies.\n")
        f.write("   Run the development server: python manage.py runserver\n")

def setup_jwt(project_name):
    """Add JWT authentication setup."""
    settings_path = os.path.join(project_name, project_name, 'settings.py')
    with open(settings_path, 'a') as f:
        f.write("\n# JWT Authentication\n")
        f.write("INSTALLED_APPS += ['rest_framework', 'rest_framework_simplejwt']\n")
        f.write("REST_FRAMEWORK = {\n")
        f.write("    'DEFAULT_AUTHENTICATION_CLASSES': (\n")
        f.write("        'rest_framework_simplejwt.authentication.JWTAuthentication',\n")
        f.write("    ),\n")
        f.write("}\n")

def setup_token_auth(project_name):
    """Add token-based authentication setup."""
    settings_path = os.path.join(project_name, project_name, 'settings.py')
    with open(settings_path, 'a') as f:
        f.write("\n# Token-based Authentication\n")
        f.write("INSTALLED_APPS += ['rest_framework', 'rest_framework.authtoken']\n")
        f.write("REST_FRAMEWORK = {\n")
        f.write("    'DEFAULT_AUTHENTICATION_CLASSES': (\n")
        f.write("        'rest_framework.authentication.TokenAuthentication',\n")
        f.write("    ),\n")
        f.write("}\n")

def setup_google_login(project_name):
    """Add Google login setup."""
    settings_path = os.path.join(project_name, project_name, 'settings.py')
    with open(settings_path, 'a') as f:
        f.write("\n# Google Login\n")
        f.write("INSTALLED_APPS += ['allauth', 'allauth.account', 'allauth.socialaccount', 'allauth.socialaccount.providers.google']\n")
        f.write("AUTHENTICATION_BACKENDS = (\n")
        f.write("    'django.contrib.auth.backends.ModelBackend',\n")
        f.write("    'allauth.account.auth_backends.AuthenticationBackend',\n")
        f.write(")\n")

def setup_redis(project_name):
    """Add Redis setup."""
    settings_path = os.path.join(project_name, project_name, 'settings.py')
    with open(settings_path, 'a') as f:
        f.write("\n# Redis Cache\n")
        f.write("CACHES = {\n")
        f.write("    'default': {\n")
        f.write("        'BACKEND': 'django_redis.cache.RedisCache',\n")
        f.write("        'LOCATION': 'redis://127.0.0.1:6379/1',\n")
        f.write("        'OPTIONS': {\n")
        f.write("            'CLIENT_CLASS': 'django_redis.client.DefaultClient',\n")
        f.write("        }\n")
        f.write("    }\n")
        f.write("}\n")

def setup_docker(project_name):
    """Add Docker setup."""
    # Create Docker files
    with open(os.path.join(project_name, 'Dockerfile'), 'w') as f:
        f.write("FROM python:3.8\nWORKDIR /app\nCOPY . /app\nRUN pip install -r requirements.txt\nCMD ['python', 'manage.py', 'runserver', '0.0.0.0:8000']\n")
    
    with open(os.path.join(project_name, 'docker-compose.yml'), 'w') as f:
        f.write("version: '3'\nservices:\n  web:\n    build: .\n    ports:\n      - '8000:8000'\n    volumes:\n      - .:/app\n    environment:\n      - DEBUG=1\n")

def setup_swagger(project_name):
    """Add Swagger documentation setup."""
    settings_path = os.path.join(project_name, project_name, 'settings.py')
    with open(settings_path, 'a') as f:
        f.write("\n# Swagger Documentation\n")
        f.write("INSTALLED_APPS += ['drf_yasg']\n")

def setup_file_uploads(project_name):
    """Integrate Cloudinary/AWS S3 for file uploads."""
    settings_path = os.path.join(project_name, project_name, 'settings.py')
    with open(settings_path, 'a') as f:
        f.write("\nimport os\n") 
        f.write("\n# Cloudinary/AWS S3 for file uploads\n")
        f.write("INSTALLED_APPS += ['cloudinary', 'storages']\n")
        f.write("DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'\n")
        f.write("AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')\n")
        f.write("AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')\n")
        f.write("AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')\n")
        f.write("\n# Add allauth account middleware\n")
        f.write("MIDDLEWARE += ['allauth.account.middleware.AccountMiddleware']\n")

def configure_secure_cookies(project_name):
    """Configure secure cookies."""
    settings_path = os.path.join(project_name, project_name, 'settings.py')
    with open(settings_path, 'a') as f:
        f.write("\n# Secure Cookies\n")
        f.write("SESSION_COOKIE_SECURE = True\n")
        f.write("CSRF_COOKIE_SECURE = True\n")

def create_new_app(project_name, app_name):
    """Create a new Django app."""
    subprocess.run(['python', 'manage.py', 'startapp', app_name], cwd=project_name)
    settings_path = os.path.join(project_name, project_name, 'settings.py')
    with open(settings_path, 'a') as f:
        f.write(f"\nINSTALLED_APPS += ['{app_name}']\n")
    
    # Ensure the app directory exists
    app_dir = os.path.join(project_name, app_name)
    os.makedirs(app_dir, exist_ok=True)
    
    # Create urls.py in the new app
    urls_path = os.path.join(app_dir, 'urls.py')
    with open(urls_path, 'w') as f:
        f.write("from django.urls import path\n")
        f.write("from . import views\n\n")
        f.write("urlpatterns = [\n")
        f.write("    # Define your app's URL patterns here\n")
        f.write("]\n")

cli.add_command(init)

if __name__ == '__main__':
    cli()