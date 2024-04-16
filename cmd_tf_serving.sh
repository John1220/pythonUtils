## aliyun
mkdir /home/serving
cd /home/serving/
wget https://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo -O /etc/yum.repos.d/docker-ce.repo
yum -y install docker-ce-20.10.21
systemctl enable docker && systemctl start docker
docker --version
#docker pull tensorflow/serving:2.8.0
# docker run -t --rm -p 8501:8501 -v "/home/serving/pb_model:/models" tensorflow/serving:2.8.0 --model_config_file=/models/models.config --enable_batching=true --batching_parameters_file=/models/batching.conf &
yum -y install htop
yum -y install git

## tf-serving
docker run -t --rm -p 8531:8501 -v "/home/serving/pb_model:/models" tensorflow/serving:2.8.0 --model_config_file=/models/models.config --enable_batching=true --batching_parameters_file=/models/batching.conf &

docker run -t --rm -p 8501:8501 -v "/home/serving/pb_model:/models" zh1220/tensorflow-serving --model_config_file=/models/models.config --enable_batching=true --batching_parameters_file=/models/batching.conf &

docker run -t --rm -p 8601:8501 -v "/home/serving/pb_model:/models" zh1220/tensorflow-serving --model_config_file=/models/models.config --enable_batching=true --batching_parameters_file=/models/batching.conf &

locust -f locu.py --host=http://192.168.199.72:8501
tools/run_in_docker.sh -d tensorflow/serving:2.8.3-devel bazel build tensorflow_serving/...

docker build -t $USER/tensorflow-serving --build-arg TF_SERVING_BUILD_IMAGE=$USER/tensorflow-serving-devel -f tensorflow_serving/tools/docker/Dockerfile .

docker build --pull -t $USER/tensorflow-serving-devel -f tensorflow_serving/tools/docker/Dockerfile.devel .

docker build -t zh1220/tensorflow-serving \
  -f tensorflow_serving/tools/docker/Dockerfile .

docker run -t --rm -p 8501:8501 -v "/home/serving/pb_model:/models" tensorflow/serving:latest-devel --model_config_file=/models/models.config --enable_batching=true --batching_parameters_file=/models/batching.conf &
