# Setup Spark Slave 
in ubuntu i will fist i will install pip 
```shell
apt install python3-pip
```
then i will install nessary packages 
```shell
pip install py4j notebook
```

to install spark u must first install packages 
```shell
sudo apt install default-jdk scala git -y
```
then to check 
```shell
java -version; javac -version; scala -version; git --version
```

now download spark packages 
```shell
wget https://dlcdn.apache.org/spark/spark-3.2.4/spark-3.2.4-bin-hadoop2.7.tgz
```
extract dir 
```shell
tar xvf spark-*
```

move to /opt
```shell
mv  spark-3.2.4-bin-hadoop2.7 /opt/spark
```

add to var_env
```shell
echo "export SPARK_HOME=/opt/spark" >> ~/.bashrc
echo "export PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin" >> ~/.bashrc
echo "export PYSPARK_PYTHON=/usr/bin/python3" >> ~/.bashrc
source ~/.bashrc
```

now start master 
```shell
./sbin/start-slave.sh spark://MASTER_IP:7077
```

