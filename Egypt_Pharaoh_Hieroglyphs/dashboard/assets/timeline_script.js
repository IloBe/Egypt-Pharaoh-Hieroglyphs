/*
 * Client-side script for the Pharaohs Timeline page.
 * This script uses a single, global event listener on the document in the
 * 'capturing' phase. This version includes specific logging to debug
 * clicks on the blue arrow as requested.
 */

console.log("Global timeline script loaded in capturing mode. Awaiting clicks.");

// Attach a single click listener to the entire document.
document.addEventListener('click', function(event) {
    
    // First, let's find the card that was clicked, if any.
    const card = event.target.closest('.timeline-card');
    
    // If a click happened inside a card...
    if (card) {
        // Now, check if the specific element that was clicked was the blue arrow.
        if (event.target.classList.contains('card-expand-arrow')) {
            // This is the message you asked for.
            console.log("SUCCESS: Blue arrow was clicked!");
        } else {
            // This tells us a click happened on the card, but not the arrow.
            console.log("INFO: A part of the timeline card (not the arrow) was clicked.");
        }
        
        // The original interactivity logic remains here.
        card.classList.toggle('is-expanded');
    }
    
}, true); // Use capturing phase to ensure it fires first