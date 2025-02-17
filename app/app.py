from fastai.vision.all import load_learner
import gradio as gr
import pathlib

temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath

bird_names = ('Crow', 
              'Duck', 
              'Eagle', 
              'Flamingo', 
              'Hawk', 
              'Hornbill', 
              'Hummingbird', 
              'Kingfisher', 
              'Owl', 'Parrot', 
              'Peacock', 
              'Pelican', 
              'Penguin', 
              'Pigeon', 
              'Robin', 
              'Seagull', 
              'Sparrow', 
              'Stork', 
              'Swallow', 
              'Woodpecker')

model = load_learner('models/cap-recognizer-v2.pkl')

def recognize_image(image):
  pred, idx, probs = model.predict(image)
  return dict(zip(bird_names, map(float, probs)))

image = gr.Image(width=250, height=250)
label = gr.Label()
examples = [
    'test_images/firstpic.jpeg',
    'test_images/secondpic.jpg',
    'test_images/thirdpic.jpeg',
    'test_images/fourthpic.jpeg',
    'test_images/fifthpic.jpeg']


iface = gr.Interface(fn=recognize_image, inputs=image, outputs=label, examples = examples)
iface.launch(inline=False,share=True)