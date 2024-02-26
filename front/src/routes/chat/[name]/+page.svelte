<script>
  import Chat from "$lib/Chat.svelte";
  export let data;
  let message = "";
  import { get_chat, submit_chat, storedname } from "$lib/common";
  import { page } from "$app/stores";
  import { invalidateAll } from "$app/navigation";
  import { css } from "styled-system/css";
</script>

<h1>You are in {$page.params.name}</h1>
{#each data.chat.messages as message}
  <div>
    {message.author}: {message.body}
  </div>
{/each}

<form
  on:submit|preventDefault={async () => {
    await submit_chat({
      chat_name: $page.params.name,
      user: $storedname,
      body: message,
    });
    message = "";
    invalidateAll();
  }}
>
  <input
    type="text"
    placeholder="chat message..."
    bind:value={message}
    class={css({
      p: "2",
      bg: "amber.500",
      rounded: "md",
      _placeholder: { color: "amber.600" },
    })}
  />
</form>


