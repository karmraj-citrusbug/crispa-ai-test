# Introduction to the crispa full stack test tasks

The test tasks are designed for you to showcase both your frontend and backend skills.

I have tried to be as comprehensive as possible in the explanations and acceptance criteria for each ticket, but if something is not clear, feel free to make a reasonable assumption.

The graphs and the data table are from the actual design for Crispa, so if we continue to work together, your first task will be to implement them in the Crispa app.

You are not expected to complete all the tickets within the 8 hours, just do as many as you can. It is up to you if you want to spend extra time on completing the remaining ones.

## What I will be looking for:

- That functionality works as expected and is bug-free
- That the UI follows the design as closely as possible (and that any deviations from the design are based on reasonable considerations)
- That the code is well-structured
- That names of variables, functions classes etc. are clear and semantic
- That the code contains appropriate comments to make it easily accessible
- That the written handover is clear and concise, so I can easily run the project, run tests etc.

## Other instructions

- Don’t worry about authentication. In the Crispa app we use Auth0 for user authentication and JWT authentication for all API requests. So I don’t want you to spend time setting any of this up for this test project
- The tickets in shortcut must be handled in order, starting with #1. No skipping. Move tickets to in progress and done as appropriate
- There must be at least one commit per ticket, and it should have a meaningful commit message

## How to get started

- Clone this repo to a new repo in your own GitHub account and commit all work to that repo
- You will receive a seperate invite to the Shortcut board where you can start working on the tickets
- You will also reveive a link to a figma file with the design for the graphs and the data table as well as some general design guidelines, like colors etc. NB: For the fonts, use the Google fonts mentioned in the styleguide in Figma. The actual font used in the Figma file is a paid font.
- Run the project with `docker-compose up --build`
- Django migrations are performed automatically when the project is started
- The frontend is served on `localhost:3000` and the backend on `localhost:8000`
- You should see 'Hello World' in the browser on `localhost:3000` and on `localhost:8000/api/hello` you should see a json response with 'Hello World'

## Handover

- Replace this readme text with a brief written handover of the project. This should include:
  - How to run the project
  - Any instructions needed to run the tests
  - Any other relevant information
- Make sure to push the code to your GitHub repo and send me the link to it in the chat on upwork
