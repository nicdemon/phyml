# PhyML web interface project

As mentionned in the [main branch of the repo](https://github.com/nicdemon/phyml), this version is the web version hosted on the [Streamlit community cloud](https://nhm4xkxjr44nwhx5zkugmj.streamlit.app/).

The project is a remake of the first version using Streamlit for web app GUI and MongoDB for analysis history.

## Dependency
All dependencies for this project are in the `requirements.txt` file.

## Execution
The app is hosted on the Streamlit community cloud.

Should the user want to use a local version of the app, it can be done with the following command after having cloned the repo:
```
streamlit run Phyml.py
```
Afterwards, the web interface can be accessed in a web browser at the address `localhost:8501` or any other port given by the streamlit server.