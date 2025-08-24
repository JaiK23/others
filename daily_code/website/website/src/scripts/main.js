// This file contains the JavaScript code for the website. It handles interactivity, DOM manipulation, and any client-side logic required for the website's functionality.

document.addEventListener('DOMContentLoaded', () => {
    const welcomeMessage = document.getElementById('welcome-message');
    if (welcomeMessage) {
        welcomeMessage.textContent = 'Welcome to our website!';
    }

    const button = document.getElementById('action-button');
    if (button) {
        button.addEventListener('click', () => {
            alert('Button clicked!');
        });
    }
/*
<button id="action-button">Click Me</button> <!-- c: required for JS to bind -->
            <button id="Track expense">To track expense</button>
            <button id="Set Budget">To track expense</button> //Add dropdown for montly , weekly and daily
            <button id="Show visualization">To track expense</button>
            <button id="Add bought items manually">To track expense</button>
*/
    const trackBTN = document.getElementById('track-expense');

    if (trackBTN) {
        trackBTN.addEventListener('click', () => {
            //Implement basic functions
            console.log("Tracked Expense successfully");
        })
    }

    const setBudgetBTN = document.getElementById('set-budget');
    if(setBudgetBTN){
        setBudgetBTN.addEventListener('click', () =>{
            //daily
            console.log("Budget set successfully");
            //monthly
            
            //weekly
        })
    }

    const showVisBTN = document.getElementById('show-vis');
    if(showVisBTN){
        showVisBTN.addEventListener('click', () =>{
            //
            console.log("Visualized successfully");
        })
    }

    const manualAddBTN = document.getElementById('manual-add');
    if(manualAddBTN){
        manualAddBTN.addEventListener('click', () =>{
            //
            console.log("Budget set successfully");
        })
    }
});