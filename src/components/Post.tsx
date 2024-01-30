import { createResource } from "solid-js";

export interface PostProps {
  id: number,
  title: string;
  content: string;
  user_id: number;
  username: string;
  email: string;
  created_at: string;
  updated_at: string;
}

export default function Post({ post }: { post: PostProps }) {
  return <div class="flex flex-row items-start justify-start gap-3 px-5 py-6 bg-zinc-100 w-full rounded-md">

    <div class="flex flex-col gap-1 text-md items-center">
      <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#404040" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-arrow-big-up"><path d="M9 18v-6H5l7-7 7 7h-4v6H9z" /></svg>
      30
      <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#404040" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-arrow-big-down"><path d="M15 6v6h4l-7 7-7-7h4V6h6z" /></svg>
    </div>

    <div class="flex flex-col items-start justify-start gap-3 w-full">
      <div class="flex flex-row items-end gap-4">
        <h1 class="text-2xl font-semibold text-gray-900">
          {post.title}
        </h1>
        <span class="text-gray-600 text-sm">
          posted by {post.username} 3 days ago
        </span>
      </div>

      <div class="relative">
        <p class="text-lg max-h-[80px] overflow-clip">
          {post.content}
        </p>
        <div class="absolute bg-gradient-to-t from-zinc-100 from-10% p-4 -bottom-2 w-full"></div>
      </div>

      <div class="py-4 flex flex-row justify-start items-center gap-4 w-full">
        <div class="flex flex-row items-center justify-start gap-2">
          <svg xmlns="http://www.w3.org/2000/svg" width="21" height="21" viewBox="0 0 24 24" fill="none" stroke="#404040" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-message-square"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z" /></svg>
          32 Comments
        </div>
        <div class="flex flex-row items-center justify-start gap-2">
          <img height={21} width={21} src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIiBzdHJva2U9IiM0MDQwNDAiIHN0cm9rZS13aWR0aD0iMiIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBjbGFzcz0ibHVjaWRlIGx1Y2lkZS1yZWRvIj48cGF0aCBkPSJNMjEgN3Y2aC02Ii8+PHBhdGggZD0iTTMgMTdhOSA5IDAgMCAxIDktOSA5IDkgMCAwIDEgNiAyLjNsMyAyLjciLz48L3N2Zz4=" />
          Share
        </div>
        <div class="flex flex-row items-center justify-start gap-2">
          <img height={21} width={21} src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIiBzdHJva2U9IiM0MDQwNDAiIHN0cm9rZS13aWR0aD0iMiIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBjbGFzcz0ibHVjaWRlIGx1Y2lkZS1ib29rbWFyayI+PHBhdGggZD0ibTE5IDIxLTctNC03IDRWNWEyIDIgMCAwIDEgMi0yaDEwYTIgMiAwIDAgMSAyIDJ2MTZ6Ii8+PC9zdmc+" alt="Save icon" srcset="" />
          Save
        </div>
      </div>
    </div>

  </div>
}
