FROM registry.gitlab.com/cloudybay/cb_dood/centos7python36


ARG TMP_PROJECT_DIR=/tmp/project

COPY __setup/requirements.txt $TMP_PROJECT_DIR/__setup/


######### custom script to install package... #########

RUN pip3.6 install -r $TMP_PROJECT_DIR/__setup/requirements.txt


#######################################################

# environ settings
ENV LC_ALL=en_US.utf8 \
    LANG=en_US.UTF-8 \
    LANGUAGE=en_US.UTF-8


COPY . $TMP_PROJECT_DIR

RUN mkdir $TMP_PROJECT_DIR/logfiles || true

RUN cp -f $TMP_PROJECT_DIR/env.readme $TMP_PROJECT_DIR/env.py

ARG IMAGE_PROJECT_DIR
RUN mkdir -p $IMAGE_PROJECT_DIR

RUN groupadd -r cloudybay && useradd -m -g cloudybay cloudybay
RUN chown -R cloudybay:cloudybay $IMAGE_PROJECT_DIR
RUN chown -R cloudybay:cloudybay $TMP_PROJECT_DIR

USER cloudybay

WORKDIR $IMAGE_PROJECT_DIR

ENTRYPOINT ["/tmp/project/entrypoint.sh"]