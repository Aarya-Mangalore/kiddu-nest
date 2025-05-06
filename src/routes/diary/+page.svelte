<script>
  import BookBg from "$lib/components/EmojiBackground.svelte";
  import DiaryCard from "$lib/components/DiaryCard.svelte";
  import { goto } from '$app/navigation';
  import Papa from 'papaparse';

  let entries = [];

  // Fetch CSV from Google Sheets
  async function fetchDiaryEntries() {
      const response = await fetch('https://docs.google.com/spreadsheets/d/e/2PACX-1vQ1s8WJrb-vnBKuTXWDILuQC8gXgNRtt1hpAio1zfyPdyFKpfOx5D3KvfgxXog86pVPsVaCBj0n1VAS/pub?output=csv');
      const csvText = await response.text();
      
      // Parse the CSV text into an array
      Papa.parse(csvText, {
          header: true,
          skipEmptyLines: true,
          complete: function(results) {
              // Map entries with a unique 'id' for each entry
              entries = results.data.map((entry, index) => ({
                  ...entry,
                  id: index // Using index as a unique ID
              })).reverse();  // Reverse the order to display newest first
          }
      });
  }

  // Fetch entries when component mounts
  import { onMount } from 'svelte';
  onMount(fetchDiaryEntries);

  function handleAddEntry() {
      goto('/add-entry');
  }
</script>

<BookBg emoji='📚' bgcolor='rgba(240, 230, 170, 0.75)' floatemoji="📕" />

<div class="diary-page">
  <h1 class="title">📚Diary page📕</h1>
  
  <!-- Add Entry Button -->
  <button class="add-entry-btn" on:click={handleAddEntry}>
    ➕ Add New Entry
  </button>

  <!-- Loop through diary entries and render DiaryCard -->
  {#each entries as entry (entry.id)}
  <DiaryCard 
    date={entry["What was today's date again? 🤔🤔"]} 
    mood={entry["Overall, Ninn mood heg ithu?"]} 
    text={entry["Heng ithu ivathin dinaa?"]} 
    image={entry["Enadru photo aitha? (please upload to Drive, give access to anyone with link and add link.)"]?.trim() || null}
    audio={entry["Song issta aythu illa enadru helbeka ?? (please upload to Drive, give access to anyone with link and add link.)"]?.trim() || null}
  />
{/each}

</div>

<style>
.diary-page {
  display: flex;
  flex-direction: column;
  align-items: center;
  min-height: 100vh;
  padding-top: 2rem;
}

.title {
  font-size: 2.5rem;
  font-weight: bold;
  color: #ff69b4;
  margin-bottom: 10px;
  text-align: center;
}

.add-entry-btn {
  background: linear-gradient(135deg, #ff69b4, #ffc0cb);
  color: white;
  border: none;
  padding: 0.75rem 1.5rem;
  font-size: 1.1rem;
  border-radius: 9999px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.25);
  cursor: pointer;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
  margin-bottom: 2rem;
  z-index: 10;
}

.add-entry-btn:hover {
  transform: scale(1.05);
  box-shadow: 0 6px 14px rgba(0, 0, 0, 0.3);
}

.add-entry-btn:active {
  transform: scale(0.97);
}
</style>
