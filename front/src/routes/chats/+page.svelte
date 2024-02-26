<script>
  export let data;
  import { get_chats, create_chat, storedname } from "$lib/common";
  import { invalidateAll } from "$app/navigation";
  let chatName;
  import { css } from "styled-system/css";
</script>

{#if data.chats.length > 0}
  {#each data.chats as chat}
    <div>
      <a href="/chat/{chat.name}">{chat.name}</a>
    </div>
  {/each}
{:else}
  No chats
{/if}
<button
  class={css({ background: "amber.500", rounded: "md", p: 2 })}
  on:click|preventDefault={async () => {
    await create_chat({ owner: $storedname, name: data.emoji });
    await invalidateAll();
  }}>create chat {data.emoji}</button
>
<div>
  Enter chat name: <input
    type="text"
    bind:value={chatName}
    class={css({ p: "2", bg: "amber.500", rounded: "md" })}
  /><button
    class={css({ background: "amber.500", rounded: "md", p: 2 })}
    on:click={async () => {
      await create_chat({ owner: $storedname, name: chatName });
      await invalidateAll();
    }}>Submit</button
  >
</div>
