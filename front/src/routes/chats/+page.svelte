<script>
  export let data;
  import { get_chats, create_chat, storedname } from "$lib/common";
  import { invalidateAll } from "$app/navigation";
</script>

<div><a href="/">Main</a></div>

List chats

{#if data.chats.length > 0}
  Got chats
  {#each data.chats as chat}
    <div>
      <a href="/chat/{chat.name}">{chat.name}</a>
    </div>
  {/each}
{:else}
  No chats
{/if}
<button
  on:click|preventDefault={async () => {
    await create_chat({ owner: $storedname, name: data.emoji });
    await invalidateAll();
  }}>create chat {data.emoji}</button
>
