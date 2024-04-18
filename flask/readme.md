# Tensorflow Flask Demo

## Getting started

   1. Follow these instructions (up to "Create and Run a minimal Flask app")
   [VS Code Flask Tutorial](https://code.visualstudio.com/docs/python/tutorial-flask#_create-a-project-environment-for-the-flask-tutorial)

   2. Run the following code:

   ```shell
  pip install tensorflow
  pip install pandas
   ```

## Running the site

Run the following command:

```shell
python -m flask run --port=8000
```

## Executing predictions

From your browser, navigate to: <http://localhost:8000/?x={YOUR_INTEGER_VALUE_HERE}>

For example, try the following: <http://localhost:8000/?x=7>

## Using the Docker Image

Run the following command:
[Docker Image](https://hub.docker.com/r/ikemtz/tensor-flask-demo)

```shell
docker pull ikemtz/tensor-flask-demo:latest
docker run --rm -it -p 8000:8000/tcp ikemtz/tensor-flask-demo:latest
```

## Hosted instance

**Note**: This is a temporary instance, uptime is not gauranteed.  Additionally, this site, is based on the container image: <https://hub.docker.com/r/ikemtz/tensor-flask-demo>.

URL: <https://ikemtz-tensorflow.azurewebsites.net/?x=6>
