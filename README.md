# Singro
Music Producers often dont have access to amazing vocals, or it can be extremely hard to find that voice it perfectly suits your track . This web app main goal is to solve that problem . Its goal is to bring music producers and songwriters in a single online space to share information , music , and mainly collaborate together .

Important Note : Although the application is considered to be a simpler version of a social media website , I decided to take an approach to the application based on some stages of the software development cycle . This allowed me to get familiar with the SDLC and take a good idea and develop it into a good , well thought piece of software .

I focused mainly on the following stages for the application : 
       1. Planning and coming with a min set of requirements 
       2. Focusing an UI and UX design and a prototype with Figma 
       3. Software development , implementing the prototype ^  using Django as my main web framework , and HTML .CSS , Javascript for front end implementation.
       4. Testing , and deployment.
  
## Planning and Initial Set of Requirements 
The websites initial functionalities will be to :
  - Create an account for any user , using django built int User authorization model and flow .
  - Make posts , comments , sharing such as blog functionality  .
  - Create songs/groups where user can add posts and also be part of .
  - Allow an user , such as a Music producer to join a song/group to interact with the creator
  
Current technologies used :

          Back end : 
                - Django , a Python web framework 
                    - concepts used such as : templates, class based views , function views , url settings , user authentication , etc.
          Front end :
                 -HTML(template tagging , etc) , CSS , and Javascript .
          Deployment (future) 
                 - Deployment to be determined using PythonAnywhere 
                 
          UI and UX implementation : 
                - Figma 
## UI/UX Approach 

Current technologies used :

          Sketching : 
                - Concepts iPad Version 
          User Flows:
                - Figma  
          Wireframes, Mockups , Prototypes: 
                - Figma 

All of the work for the design section and its corresponding procedures can be found in the UI:UX Files folder .

The main design process started from sketching , user flows , sitemap, wireframing , and finally prototyping .

### Sketching 
During the sketching process i focused on generating initial ideas , not worrying too much about specific details of the design. Taking into consideration the main requirements i just sketched possible user flows , stories from perhaps a beginning to an end , etc. There is really not a specific rule for this part of the design process , but to just generate as much possible ideas . From here i can start creating something more formal that describe specific goals through user flows .

Here is my main sketches , produced on my Ipad 2 Concepts App : 

![Singro Sketching ](https://raw.githubusercontent.com/nicocoa10/singro/master/UI%3AUX%20Files/Sketching_0/all.jpg)

### User Flows 
After having generating some ideas that meet some of the requirements i get a more clear idea of specific goals and paths the user should take in order to fulfill a certain action or goal . This is where i started creating user flow diagrams that describe each page and the action that takes you to the next , until a goal is reached .

Here is an example of joining groups and its user flow , 

![Singro User Flows ](https://raw.githubusercontent.com/nicocoa10/singro/master/UI%3AUX%20Files/User%20Flows_1/Screen%20Shot%202021-07-30%20at%2010.53.58%20PM.png)

### Sitemaps 

After i generated user flows , i had a good idea of how many pages the application will be composed of . Then a sitemap allows us to see a hierarchical diagram of the page structure , and see what leads to what .

![Singro Sitemap ](https://raw.githubusercontent.com/nicocoa10/singro/master/UI%3AUX%20Files/Site%20Map/Screen%20Shot%202021-07-30%20at%2010.59.18%20PM.png)

### Wireframing
Wireframes are low fidelity designs that allowed me to be way more detailed than my previous made sketches . Knowing and having an idea of number of pages , and user flows i then started creating designs with focus on layout , and if they meet user goals . Also i can worry now more about specific details such as text for example . My wireframes are still not the final design but its a more detailed design than the sketches .

Here is an example of my home page wireframe,

![Singro home wireframe ](https://raw.githubusercontent.com/nicocoa10/singro/master/UI%3AUX%20Files/Wireframes_2/Screen%20Shot%202021-07-30%20at%2011.04.46%20PM.png)

### Prototyping and Final Design

This is were i focused mainly on all details of each page , including colors , layout , structure , fonts , positioning , and usability . It was important to take into consideration all of the past designs , and feedback and apply it to the final design . Technically by this point the design aspect of the app has been well thought already , and many mistakes and errors have been caught throughout the process.

Final Designs Prototypes :


#### Home

![Singro home wireframe ](https://raw.githubusercontent.com/nicocoa10/singro/master/UI%3AUX%20Files/Prototype_4/Screen%20Shot%202021-07-30%20at%2011.09.52%20PM.png)

#### Sign Up

![Singro sign up prototype ](https://raw.githubusercontent.com/nicocoa10/singro/master/UI%3AUX%20Files/Prototype_4/Sign%20Up.png)

#### Log In

![Singro log in prototype](https://raw.githubusercontent.com/nicocoa10/singro/master/UI%3AUX%20Files/Prototype_4/Login.png)

#### User Profile

![Singro user profile prototype](https://raw.githubusercontent.com/nicocoa10/singro/master/UI%3AUX%20Files/Prototype_4/User%20Page.png)



## Development Approach 

Current technologies used :

          Back end : 
                - Django , a Python web framework 
                    - concepts used such as : templates, class based views , function views , url settings , user authentication , etc.
          Front end :
                 -HTML(template tagging , etc) , CSS , and Javascript .
          Deployment (future) 
                 - Deployment to be determined using PythonAnywhere 

### Back end 

I used the Django web framework to implement all back end procedures of this app. 
I mainly focused on 3 apps(within djangos structure) which are the following , 
              
                   - accounts 
                   - groups 
                   - posts 
Each of the following above apps are in charge of specific tasks . and have their corresponding templates .

#### accounts
Accounts main goal is to use Djangos user authorization models to be able to create and authorize users .
#### groups
groups app uses several class based views in order to create groups and allow users to join a specifc group . Each group is composed of posts . 
#### posts
posts allows users to create posts and group them by name . A specific authorized user can create a post then select which group the user wants to post to .

 Change log :
Currently the initial functionalities of the project have been implmented in the back end for making posts funtionality . All required views have been made and urls set up correctly. 11/19/20

The project now contains full functonality to create accounts , make a group/song , join a group/song and make a post . 6/19/21  

I realized that i will need more information from an user , and eventually to build a profile with more information so i will need an custom user model . I been working on creating my own user model . 6/19/21                  


### Front End 

I have spent a good amount of time building the design generated from the UI section of this project . I use only HTML , CSS and Javascript to build and construct the design by scratch . Some design things such as positioning of images changed along the development process . This was in order to fulfill other design requirements that came about when developing the front end of the app. 

I focused on developing a design that is responsive for all screen types.

Technologies and external libraries i ended up using : 

                            - Bootstrap 4 
                            
As i build the application ill keep updating this page , but this is the progress of the front end pages 

#### Home Page

(GIF images may look blurry)
##### Desktop
![Singro home desktop  ](https://raw.githubusercontent.com/nicocoa10/sat337-test/master/ezgif.com-gif-maker.gif)


##### Mobile
![Singro home mobile ](https://github.com/nicocoa10/sat337-test/blob/master/ezgif.com-gif-maker%20(1).gif?raw=true)

#### Login Page 
![Singro login ](https://raw.githubusercontent.com/nicocoa10/sat337-test/master/Screen%20Shot%202021-08-11%20at%202.25.33%20PM.png)

#### Sign up Page 
![Singro login ](https://raw.githubusercontent.com/nicocoa10/sat337-test/master/Screen%20Shot%202021-08-11%20at%202.25.50%20PM.png)


#### Profile Page 
![Singro profile ](https://raw.githubusercontent.com/nicocoa10/sat337-test/master/Screen%20Shot%202021-08-24%20at%206.55.12%20PM.png)



                 

        



        
