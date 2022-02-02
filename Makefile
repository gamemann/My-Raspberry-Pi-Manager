install:
	cp scripts/raspi_manager.service /etc/systemd/system
	mkdir -p /etc/raspi_manager
	cp -n scripts/uwsgi_production.ini /etc/raspi_manager