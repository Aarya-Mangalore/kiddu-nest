<script>
    import { onMount } from "svelte";
    let notes = [];
    let newNoteText = "";
    
    async function fetchNotes() {
        const res = await fetch("http://127.0.0.1:5000/notes");
        notes = await res.json();
    }

    async function addNote() {
        if (!newNoteText) return;
        await fetch("http://127.0.0.1:5000/notes", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ text: newNoteText }),
        });
        newNoteText = "";
        fetchNotes();
    }

    async function updateNote(index, text) {
        await fetch(`http://127.0.0.1:5000/notes/${index}`, {
            method: "PUT",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ text }),
        });
        fetchNotes();
    }

    async function deleteNote(index) {
        await fetch(`http://127.0.0.1:5000/notes/${index}`, { method: "DELETE" });
        fetchNotes();
    }

    onMount(fetchNotes);
</script>

<style>
    .container {
        width: 80%;
        margin: auto;
        text-align: center;
    }
    .note {
        background: white;
        padding: 15px;
        margin: 10px;
        border-radius: 10px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        text-align: left;
        position: relative;
    }
    .note textarea {
        width: 100%;
        border: none;
        font-size: 1rem;
    }
    .buttons {
        position: absolute;
        top: 10px;
        right: 10px;
    }
    button {
        margin-left: 10px;
        cursor: pointer;
        padding: 5px 10px;
        border: none;
        background: #ff6b6b;
        color: white;
        border-radius: 5px;
    }
    button.edit {
        background: #4caf50;
    }
    .add-note {
        margin-bottom: 20px;
        display: flex;
        justify-content: center;
        gap: 10px;
    }
    input {
        padding: 10px;
        width: 300px;
        border: 1px solid #ccc;
        border-radius: 5px;
    }
</style>
<br>
<br>
<br>
<div class="container">
    <div class="add-note">
        <input bind:value={newNoteText} placeholder="Write a new note..." />
        <button on:click={addNote}>Add</button>
    </div>

    {#each notes as note, index}
        <div class="note">
            <div class="buttons">
                <button class="edit" on:click={() => updateNote(index, note.Text)}>Save</button>
                <button on:click={() => deleteNote(index)}>Delete</button>
            </div>
            <p><strong>{note.Date}</strong></p>
            <textarea bind:value={note.Text}></textarea>
        </div>
    {/each}
</div>
