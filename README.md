# BirdRecognizer
An image classification model from cleaning, data collection, model training, deployment and API integration.<br/>
The model can classify 20 different types of birds and they are: <br/>
1. Sparrows
2. Pigeons
3. Crows
4. Parrots
5. Eagles
6. Owls
7. Kingfishers
8. Peacocks
9. Ducks
10. Woodpeckers
11. Seagulls
12. Flamingos
13. Hummingbirds
14. Pelicans
15. Hawks
16. Penguins
17. Storks
18. Hornbills
19. Swallows
20. Robins

# Data processing and construction
**Data Gathering**: Download from DuckDuckgo using term name <br/>
**DataLoader**: Used fastai DataBlock API to set up the Dataloader <br/>
**Data Augmentation**: fastai provides default augmentation which operates in GPU <br/>
# Training and Cleaning
**Training**: Fined tuned a resnet50 model for 6 epochs (3 times) and got ~88% accuracy. <br/>
**Data Cleaning**: This part took me the highest time. Since I collected data from Google Images, there were many noises. Also, some images contained animation and CGI, which is not my goal right now for this project. I cleaned and updated data using fastai ImageClassifierCleaner. I cleaned the data each time after training or fine-tuning, except for the last time which was the final iteration of the model<br/>

I deployed to model to HuggingFace Spaces Gradio App. The implementation can be found in `documentation` or [here](https://huggingface.co/spaces/Faiyaz10/Bird-Recognizer)<br/>
<img src="app/Screenshot 2025-02-18 192607.png" width="800" height="350">
# Model Deployment
I deployed to model to HuggingFace Spaces Gradio App. The implementation can be found in `documentation` or [here](https://huggingface.co/spaces/Faiyaz10/Bird-Recognizer)<br/>
