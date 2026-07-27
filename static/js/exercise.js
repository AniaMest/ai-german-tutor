const choices = document.querySelectorAll(".choice-word");

choices.forEach(choice => {

    choice.addEventListener("click", () => {

        const group = choice.closest(".choice-group");

        const alreadySelected = choice.classList.contains("selected");

        group.querySelectorAll(".choice-word").forEach(word => {
            word.classList.remove("selected");
        });

        if (!alreadySelected) {
            choice.classList.add("selected");
        }

    });

});


const checkButton = document.getElementById("check-btn");

checkButton.addEventListener("click", () => {

    const groups = document.querySelectorAll(".choice-group");

    groups.forEach(group => {

        const selected = group.querySelector(".choice-word.selected");

        if (!selected) {
            return;
        }

        const correctAnswer = group.dataset.answer;
        const chosenAnswer = selected.dataset.choice;

        if (chosenAnswer === correctAnswer) {

            selected.classList.add("correct");

        } else {

            selected.classList.add("incorrect");

        }

    });

});