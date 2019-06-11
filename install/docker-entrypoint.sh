# Make logs
echo "Make log dir"
mkdir -p /apisrv/HogWhat/logs &&\
chmod 777 -R /apisrv/HogWhat/logs

# Collect static files
python3 manage.py collectstatic --noinput

# Start server
echo "Starting server"
/usr/bin/supervisord -n