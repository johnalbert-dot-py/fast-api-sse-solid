import { For, createEffect, createSignal, onCleanup } from "solid-js";
import Post from "./components/Post"
import { v4 as uuidv4 } from 'uuid';

function App() {

  const [posts, setPosts] = createSignal([]);

  createEffect(() => {
    const eventSource = new EventSource(`/api/stream?id=${uuidv4()}`);
    eventSource.addEventListener("new_posts", (data) => {
      if (data.data === posts()) return;
      const post = data.data
      setPosts(JSON.parse(post))
    })
    onCleanup(() => {
      eventSource.close();
    })
  })

  return (
    <main class="p-8 mx-auto w-full max-w-7xl ">
      <section class="">
        <h1 class="text-3xl">
          Realtime Thread Post
        </h1>

        <p class="mt-2 text-lg text-gray-600">
          This is a thread where it has different realtime feature such as posts, comments, and likes.
        </p>
      </section>

      <section class="mt-2 flex flex-col w-full justify-start items-start gap-4">

        <For each={posts()} fallback={<div>Loading...</div>} >
          {(post) => <Post post={post} />}
          {/* <Post /> */}
        </For>
      </section>
    </main >
  )
}

export default App
