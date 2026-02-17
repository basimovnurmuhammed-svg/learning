// Get DOM elements
const taskInput = document.getElementById('taskInput');
const addBtn = document.getElementById('addBtn');
const taskList = document.getElementById('taskList');
const totalCount = document.getElementById('totalCount');
const doneCount = document.getElementById('doneCount');
const clearAllBtn = document.getElementById('clearAllBtn');

let tasks = []; // Array to store tasks

// Function to update the UI
function render() {
    taskList.innerHTML = "";
    let completed = 0;

    tasks.forEach(task => {
        if (task.completed) completed++;
        const li = document.createElement('li');
        if (task.completed) li.classList.add('completed');

        li.innerHTML = `
            <span onclick="toggleTask(${task.id})" style="cursor:pointer; flex:1;">${task.text}</span>
            <button class="delete-btn" onclick="removeTask(${task.id})">Delete</button>
        `;
        taskList.appendChild(li);
    });

    totalCount.textContent = tasks.length;
    doneCount.textContent = completed;
    console.log(`Rendered: ${tasks.length} tasks`); // Debug Log
}

// Add task
function addTask() {
    const text = taskInput.value.trim();
    if (text === "") return;

    const task = { id: Date.now(), text, completed: false };
    tasks.push(task);
    taskInput.value = "";
    render();
}

// Global functions for inline HTML events
window.toggleTask = (id) => {
    tasks = tasks.map(t => t.id === id ? {...t, completed: !t.completed} : t);
    render();
};

window.removeTask = (id) => {
    tasks = tasks.filter(t => t.id !== id);
    render();
};

// Event listeners
addBtn.addEventListener('click', addTask);
taskInput.addEventListener('keypress', (e) => { if (e.key === 'Enter') addTask(); });
clearAllBtn.addEventListener('click', () => { tasks = []; render(); });

console.log("Interactive Todo initialized.");
