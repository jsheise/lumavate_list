# List Project for Lumavate Candidacy

Steps to run (development server):
 - clone repo
 - cd into '/Candidate_Project'
 - run listapp.py to start development server
 - navigate to 'localhost:5000' in browser

If time allows, I will pursue the following additions:
 - implement PostgreSQL database for entry storage
 - Angular Material for design (further on Lumavate tech stack)
 - Redis caching (further on Lumavate tech stack)
 - use Discogs API to retrive album cover art

Update 5/28/19 5:40pm:
 - back-end API with Flask has been added, though the Angular framework has seemingly stopped working due to the change
   - downloaded angular.min.js from the web, rather using the CDN (this was done by a Flask explanation on substituting brackets for Angular)
   - modified tree structure
   - changed Angular brackets to '{a' and 'a}'
 - would also like to declare escape chars as constants in separate file, though not priority
 - current goal is to get angular
 - if possible, I am going to use the flask-restful package to make development of REST components
 
Update 5/28/19 7:00pm:
 - fixed above issue, see commits for details
 - potentially worth noting that I am back to using CDN for Angular, as that was not an issue
