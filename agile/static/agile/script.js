const base = document.querySelector('.card-front'); 
const enCours = document.querySelector('#EnCours');
const finis = document.querySelector('#Finis');
const aFaire = document.querySelector('#AFaire');
const box = [enCours , finis , aFaire];

let objectGrabID = null;

<<<<<<< HEAD
=======
//Put the url of the server here
const urlTacheApp = "https://testkavaldeep.azurewebsites.net/tache_app/";

>>>>>>> 39d111bf061e4c3e2e8276a0abab7e369a515f83
//base.addEventListener('dragstart' , dragStart);
base.addEventListener('dragend'  , dragEnd);

function dragStart(ev , send){
    console.log("The Drag has started");
    console.log(send);
    if(send != null){
     objectGrabID = send;
    }
    setTimeout(() => (this.className = 'invisible'), 0);
}

function dragEnd(){
     console.log("dragEndeddede ");
}


for (const vide of box ) {

    vide.addEventListener('dragenter', dragEnter);
    vide.addEventListener('dragover', dragOver);
    vide.addEventListener('dragleave', dragLeave);
   // vide.addEventListener('drop' , dragDrop);
}





function dragOver(e) {
    e.preventDefault();
}

function dragEnter(e) {
    e.preventDefault();
}

function dragLeave() {
}

function dragDrop(ev , div){
//Lorque ca a drop envoyer un message et dire dans quel categorie ca a drop
console.log("dropped");

   console.log(div);
    if(div == "EnCours")
    ChangeToEnCours(objectGrabID);
    
    else if(div == "AFaire")
    ChangeToAFaire(objectGrabID);

    else if(div == "Finis")
    ChangeToFinis(objectGrabID);
}

function ChangeToEnCours(pk)
{
    console.log(pk);

$.ajax({
   type: "POST",
<<<<<<< HEAD
   url: "http://127.0.0.1:8000/tache_app/updateTaskInProgress/",
=======
   url: urlTacheApp + "updateTaskInProgress/",
>>>>>>> 39d111bf061e4c3e2e8276a0abab7e369a515f83
   dataType: "json",
   traditional: true,
   data: {'pk' :pk },
   success: function(data) {
	   window.location.reload(true);
<<<<<<< HEAD
           console.log(data["HTTPRESPONSE"]);
=======
           console.log( "The Http response is" + data["HTTPRESPONSE"]);
>>>>>>> 39d111bf061e4c3e2e8276a0abab7e369a515f83
   			   }
  });
}

function ChangeToAFaire(pk)
{

$.ajax({
   type: "POST",
<<<<<<< HEAD
   url: "http://127.0.0.1:8000/tache_app/updateTaskToDo/",
=======
   url:  urlTacheApp + "updateTaskToDo/",
>>>>>>> 39d111bf061e4c3e2e8276a0abab7e369a515f83
   dataType: "json",
   traditional: true,
   data: {'pk' :pk },
   success: function(data) {
	   window.location.reload(true);
<<<<<<< HEAD
           console.log(data["HTTPRESPONSE"]);
=======
           console.log( "The Http response is" + data["HTTPRESPONSE"]);
>>>>>>> 39d111bf061e4c3e2e8276a0abab7e369a515f83
   			   }
  });
}

function ChangeToFinis(pk)
{

$.ajax({
   type: "POST",
<<<<<<< HEAD
   url: "http://127.0.0.1:8000/tache_app/updateTaskFinish/",
=======
   url: urlTacheApp +  "updateTaskFinish/",
>>>>>>> 39d111bf061e4c3e2e8276a0abab7e369a515f83
   dataType: "json",
   traditional: true,
   data: {'pk' :pk },
   success: function(data) {
	   window.location.reload(true);
<<<<<<< HEAD
           console.log(data["HTTPRESPONSE"]);
=======
           console.log( "The Http response is" + data["HTTPRESPONSE"]);
>>>>>>> 39d111bf061e4c3e2e8276a0abab7e369a515f83
   			   }
  });
}


