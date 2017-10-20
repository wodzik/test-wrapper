FROM droptica/php-fpm:7.1-xdebug-v1.5

RUN apt-get update && apt-get install -y libssl-dev
RUN pecl install mongodb
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
