## Inspiration
We were inspired to create this project when we saw the rise of spending on Thanksgiving dinners when that does not need to be the case.
## What it does
Our project uses AI to suggest a dish to make for Thanksgiving in a certain price range as well as an accompanying ingredients list and an image of the dish.
## How we built it
We built this app by using OpenAI's text completion and image generation models (GTP-3 and DALL·E 2) and it uses these models to create our desired outputs of an ingredients list and an image of the dish. We implemented them into Python and in a GUI with tkinter libraries.
## Challenges we ran into
Our biggest challenge was getting the text completion model to output the ingredients list in the exact format we wanted. We solved this by tuning a lot of the parameters that we used to set the model up such as the temperature. This way we were able to get outputs that made sense but were also very diverse.
## Accomplishments that we're proud of
We are very proud of how our app uses AI in a way that actually impacts the community and is not just for convenience. A lot of times AI is just used for convenience and streamlining of things but we are actually using the potential that AI has in a way that is beneficial.
## What we learned
We learned how to use OpenAI's models and integrate them into Python code. These technologies are becoming very big as of lately and the ability to easily use such powerful models will be useful in any future projects we decide to pursue.
## What's next for Thanksgiving Dinner Ideas Generator
Some improvements we could make are implementing a full recipe generator, not just the ingredients. The model also still outputs the wrong thing very rarely just because of the nature of these types of models so we will continue to work to fix that. Finally we might think of implementing this idea into a website or publishing it as an app not just as a python script because then it can actually start to impact the community.
