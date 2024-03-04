<script>
  import { PUBLIC_API } from "$env/static/public";
  import { Manager } from "socket.io-client";
  import { browser } from "$app/environment";
  const manager = new Manager(PUBLIC_API);
  const socket = manager.socket("/");

  export let data;
  let message = "";
  import { get_chat, submit_chat, subscribe, following } from "$lib/common";
  import { page } from "$app/stores";
  import { invalidateAll } from "$app/navigation";
  socket.on("new_message", () => {
    console.log("new message sent");
    if (browser) {
      invalidateAll();
    }
  });
</script>

<h1>You are in {$page.params.name}</h1>
{#each data.chat.messages as message}
  <div>
    <a href="/profile/{message.author}"> {message.author}</a>
    {#if data.friends && data.friends.includes(message.author) && message.author != data.username}
      [following]
    {/if}::
    {message.body}
  </div>
{/each}

<form
  on:submit|preventDefault={async () => {
    await submit_chat({
      chat_name: $page.params.name,
      jwt: data.jwt,
      body: message,
    });
    message = "";
  }}
>
  <input
    type="text"
    class="input"
    placeholder="chat message..."
    bind:value={message}
  />
</form>
