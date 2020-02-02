/* ----------------------------------------------------------------------
							Functions
---------------------------------------------------------------------- */

function submitAnswer(answer)
{
	let quizForm = document.forms['quizForm'];
	Array.prototype.forEach.call(quizForm.children, function(child){
		if (child.checked) {
			let obj = {name: child.name, value: child.value};
			if (JSON.stringify(obj) === JSON.stringify(answer))
			{
				alert("You got the answer RIGHT !");
			}
			else
			{
				alert("You got the answer WRONG !");
			}
		}
	});
}

function submitAnswers(answers)
{
	let total = answers.length;
	let score = 0;
	let choices = [];
	let quizForm = document.forms['quizForm'];

	Array.prototype.forEach.call(quizForm.children, function(child){
		if (child.checked) {
			let obj = {name: child.name, value: child.value};
			choices.push(obj);
		}
	});

	let rightAnswers  = choices.filter(choice => answers.some(answer => JSON.stringify(choice) === JSON.stringify(answer)));

	for(let i = 1; i <= rightAnswers.length; ++i)
	{
		++score;
	}

	if (choices.length !== answers.length)
	{
		alert('you missed a question');
		return false;
	}

	let results = document.getElementById('results');
	results.innerHTML =
		"<h3>You scored <span>"
		+ score +
		"</span> out of <span>"
		+ total +
		"</span></h3>";

	alert("You scored " + score + " out of " + total);
}
