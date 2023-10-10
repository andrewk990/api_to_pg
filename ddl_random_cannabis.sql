-- DROP TABLE IF EXISTS public.random_cannabis;

CREATE TABLE public.random_cannabis (
	  id integer 
	, uid text 
	, strain text 
	, cannabinoid_abbreviation text 
	, cannabinoid text 
	, terpene text 
	, medical_use text 
	, health_benefit text 
	, category text 
	, "type" text 
	, buzzword text 
	, brand text 
	, date_add timestamp
);

ALTER TABLE public.random_cannabis OWNER TO "postgres";