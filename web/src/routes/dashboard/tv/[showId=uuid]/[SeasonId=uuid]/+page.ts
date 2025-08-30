import { env } from '$env/dynamic/public';
import type { PageLoad } from './$types';
import client from "$lib/api";

const apiUrl = env.PUBLIC_API_URL;

export const load: PageLoad = async ({ fetch, params }) => {
	const season = await client.GET('/api/v1/tv/seasons/{season_id}', {
		fetch: fetch,
		params: {
			path: {
				season_id: params.SeasonId
			},
		}
	});
	const seasonFiles = await client.GET('/api/v1/tv/seasons/{season_id}/files', {
		fetch: fetch,
		params: {
			path: {
				season_id: params.SeasonId
			},
		}
	});
	return {
		files: seasonFiles.data,
		season: season.data
	};
};
