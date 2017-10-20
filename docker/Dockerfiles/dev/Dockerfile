FROM droptica/php-developer:7.1-v1.5

RUN apt-get update && apt-get install -y libssl-dev
RUN pecl install mongodb
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN echo "memory_limit = 1024M" > /usr/local/etc/php/conf.d/memory_limit.ini
