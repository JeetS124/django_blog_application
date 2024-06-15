echo "BUILD START"
 python3.12 -m pip install -r requirements.txt

 echo "CHANGE DIRECTORY"
cd blog_site

 echo "Make Migration..."
python3.12 manage.py makemigrations --noinput
python3.12 manage.py migrate --noinput

 python3.12 manage.py collectstatic --noinput --clear
 echo "BUILD END"
