const base = document.querySelector('.card-front'); 
const enCours = document.querySelector('#EnCours');
const finis = document.querySelector('#Finis');
const aFaire = document.querySelector('#AFaire');
const box = [enCours , finis , aFaire];

let objectGrabID = null;

//Put the url of the server here
const urlTacheApp = "http://127.0.0.1:8000/tache_app/";

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
   url: urlTacheApp + "updateTaskInProgress/",
   dataType: "json",
   traditional: true,
   data: {'pk' :pk },
   success: function(data) {
	   window.location.reload(true);
           console.log( "The Http response is" + data["HTTPRESPONSE"]);
   			   }
  });
}

function ChangeToAFaire(pk)
{

$.ajax({
   type: "POST",
   url:  urlTacheApp + "updateTaskToDo/",
   dataType: "json",
   traditional: true,
   data: {'pk' :pk },
   success: function(data) {
	   window.location.reload(true);
           console.log( "The Http response is" + data["HTTPRESPONSE"]);
   			   }
  });
}

function ChangeToFinis(pk)
{

$.ajax({
   type: "POST",
   url: urlTacheApp +  "updateTaskFinish/",
   dataType: "json",
   traditional: true,
   data: {'pk' :pk },
   success: function(data) {
	   window.location.reload(true);
           console.log( "The Http response is" + data["HTTPRESPONSE"]);
   			   }
  });
}


