<script>
  export let data;
  import { get_chats, create_chat } from "$lib/common";
  import { invalidateAll } from "$app/navigation";
  let chatName;
</script>

{#if data.chats.length > 0}
  {#each data.chats as chat}
    <div>
      <a href="/chat/{chat.name}" class="h3">{chat.name}</a>
    </div>
  {/each}
{:else}
  No chats
{/if}
<button
  class="btn variant-filled"
  on:click|preventDefault={async () => {
    await create_chat({ owner: data.username, name: data.emoji });
    await invalidateAll();
  }}>create chat {data.emoji}</button
>
<div>
  Enter chat name: <input
    type="text"
    bind:value={chatName}
    class="input"
  /><button
    on:click={async () => {
      await create_chat({ owner: data.username, name: chatName });
      await invalidateAll();
    }}>Submit</button
  >
</div>
