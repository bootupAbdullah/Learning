// four rooms: the ballroom, gallery, billiards room, and dining room,
// four weapons: poison, a trophy, a pool stick, and a knife,
// and four suspects: Mr. Parkes, Ms. Van Cleve, Mrs. Sparr, and Mr. Kalehoff.


// We also know that each weapon corresponds to a particular room, so...

// the poison belongs to the ballroom,
// the trophy belongs to the gallery,
// the pool stick belongs to the billiards room,
// and the knife belongs to the dining room.
// And we know that each suspect was located in a specific room at the time of the murder.

// Mr. Parkes was located in the dining room.
// Ms. Van Cleve was located in the gallery.
// Mrs. Sparr was located in the billiards room.
// Mr. Kalehoff was located in the ballroom.
// To help solve this mystery, write a combination of conditional statements that:

// sets the value of weapon based on the room and
// sets the value of solved to true if the value of room matches the suspect's room
// Afterwards, use this template to print a message to the console if the mystery was solved:



// / A room can be either of - dining room, gallery, ballroom, or billiards room
var room = "billiards room";

// A suspect can be either of - Mr. Parkes, Ms. Van Cleve, Mrs. Sparr, or Mr. Kalehoff
// Test your code by giving matching as well as unmatching names of the suspect
var suspect = "Mr. Parkes"; 

/* ****************************************** */

/* IMPLEMENTATION LOGIC*/

// Initial values
var weapon = "";
var solved = false;

/*
* To help solve this mystery, write a combination of conditional statements that:
* 1. sets the value of weapon based on the room and
* 2. sets the value of solved to true if the value of room matches the suspect's room
*/
if (room == "billiards room")
} else if (/* your conditional goes here */) {
    
} else if (/* your conditional goes here */) {
    
} else {
    
}
/* ****************************************** */
// The code below will run only when `solved` is true
if (solved) {
	console.log(/* your message goes here*/);
}