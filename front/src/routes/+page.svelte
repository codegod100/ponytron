<script>
  export let data;
  import { css } from "styled-system/css";
</script>

<div
  class={css({
    fontSize: "2xl",
    fontWeight: "bold",
  })}
>
  Hello 🐼!
</div>

<h2>Social</h2>

<div>Users:</div>

{#each data.users as user}
  <div>
    Username: {user.username}
  </div>
{/each}
