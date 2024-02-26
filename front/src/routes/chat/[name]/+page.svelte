<script>
  import { PUBLIC_API } from "$env/static/public";
  import { Manager } from "socket.io-client";
  const manager = new Manager(PUBLIC_API);
  const socket = manager.socket("/");

  export let data;
  let message = "";
  import { get_chat, submit_chat, subscribe, following } from "$lib/common";
  import { page } from "$app/stores";
  import { invalidateAll } from "$app/navigation";
  import { css } from "styled-system/css";
  socket.on("new_message", () => {
    console.log("new message sent");
    invalidateAll();
  });
</script>

<h1>You are in {$page.params.name}</h1>
{#each data.chat.messages as message}
  <div>
    <button
      on:click={async () => {
        await subscribe({ user: message.author, my_info: data.username });
      }}
      >{message.author}
      {#if data.friends && data.friends.includes(message.author) && message.author != data.username}
        [following]
      {/if}
    </button>: {message.body}
  </div>
{/each}

<form
  on:submit|preventDefault={async () => {
    await submit_chat({
      chat_name: $page.params.name,
      user: data.username,
      body: message,
    });
    message = "";
    // invalidateAll();
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
