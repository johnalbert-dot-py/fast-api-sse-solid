import { For, createResource } from "solid-js";
import Post from "./components/Post"

import { PostProps } from "./components/Post"

const fetchPosts = async () => {
  const res = await fetch('/api/post');
  const posts: PostProps[] = await res.json();
  console.log(posts)
  return posts;
}

function App() {

  const [posts] = createResource(fetchPosts);

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

        {
          posts.loading ? <div>Loading...</div> : <For each={posts()} >
            {(post) => <Post post={post} />}
            {/* <Post /> */}
          </For>
        }
      </section>
    </main >
  )
}

export default App
