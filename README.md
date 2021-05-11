**Matrix exercise**

At first I created 2 S3 buckets via Amazon AWS (maxims-bucket1 and maxims-bucket-2),

Then I wrote a python script which copies all the objects from maxims-bucket1 to maxims-bucket-2.

I added another file to the project that contains all the necessary credentials (secrets.py).

I set up a t3.2xlarge instace, on the instance I installed Docker and Minikube, copied all the python project to a directory called S3Sync and wrote a Dockerfile that creates an image for the python script I've written earlier.

I uploaded the image to ECR.

I created a secret in the k8s cluster that contains the password to the ecr (commands in k8ssecret.txt).

And finally I wrote a deployment.yaml file that pulls the image from the ecr and creates a pod from it that runs the python script automatically (If there is no difference between the buckets then the container wont do anything until a difference appears).

The situation I got to at the end is that every time I upload a file to maxims-bucket-1 it is copied almost immediately to maxims-bucket-2 as long as the pod are alive in the cluster.