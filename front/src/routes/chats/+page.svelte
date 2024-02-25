<script>
  import { get_chats, create_chat, storedname, randomEmoji } from "$lib/common";
  import { invalidateAll } from "$app/navigation";
  let emoji = randomEmoji();
</script>

List chats

{#await get_chats() then chats}
  {#if chats.length > 0}
    Got chats
    {#each chats as chat}
      <div>
        <a href="/chat/{chat.name}">{chat.name}</a>
      </div>
    {/each}
  {:else}
    No chats
  {/if}
  <button
    on:click|preventDefault={async () => {
      await create_chat({ owner: $storedname, name: emoji });
      invalidateAll();
    }}>create chat {emoji}</button
  >
{/await}
