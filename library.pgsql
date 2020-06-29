--
-- PostgreSQL database dump
--

-- Dumped from database version 10.12 (Ubuntu 10.12-0ubuntu0.18.04.1)
-- Dumped by pg_dump version 10.12 (Ubuntu 10.12-0ubuntu0.18.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: fareeda
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO fareeda;

--
-- Name: author; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.author (
    id integer NOT NULL,
    auth_nam character(200) NOT NULL,
    gender character(50),
    count_book integer NOT NULL
);


ALTER TABLE public.author OWNER TO postgres;

--
-- Name: author_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.author_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.author_id_seq OWNER TO postgres;

--
-- Name: author_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.author_id_seq OWNED BY public.author.id;


--
-- Name: book; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.book (
    id integer NOT NULL,
    book_name character(200) NOT NULL,
    book_issue date NOT NULL
);


ALTER TABLE public.book OWNER TO postgres;

--
-- Name: book_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.book_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.book_id_seq OWNER TO postgres;

--
-- Name: book_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.book_id_seq OWNED BY public.book.id;


--
-- Name: category; Type: TABLE; Schema: public; Owner: fareeda
--

CREATE TABLE public.category (
    id integer NOT NULL,
    name character varying NOT NULL
);


ALTER TABLE public.category OWNER TO fareeda;

--
-- Name: category_id_seq; Type: SEQUENCE; Schema: public; Owner: fareeda
--

CREATE SEQUENCE public.category_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.category_id_seq OWNER TO fareeda;

--
-- Name: category_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: fareeda
--

ALTER SEQUENCE public.category_id_seq OWNED BY public.category.id;


--
-- Name: author id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.author ALTER COLUMN id SET DEFAULT nextval('public.author_id_seq'::regclass);


--
-- Name: book id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.book ALTER COLUMN id SET DEFAULT nextval('public.book_id_seq'::regclass);


--
-- Name: category id; Type: DEFAULT; Schema: public; Owner: fareeda
--

ALTER TABLE ONLY public.category ALTER COLUMN id SET DEFAULT nextval('public.category_id_seq'::regclass);


--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: fareeda
--

COPY public.alembic_version (version_num) FROM stdin;
0b34363ba0e2
\.


--
-- Data for Name: author; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.author (id, auth_nam, gender, count_book) FROM stdin;
1	Fareeda                                                                                                                                                                                                 	F                                                 	1
2	Mohammad                                                                                                                                                                                                	M                                                 	1
4	Fareeda1                                                                                                                                                                                                	F                                                 	1
5	Fareeda1                                                                                                                                                                                                	F                                                 	1
6	Abdullah                                                                                                                                                                                                	M                                                 	2
3	Amal                                                                                                                                                                                                    	F                                                 	40
\.


--
-- Data for Name: book; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.book (id, book_name, book_issue) FROM stdin;
4	Book4                                                                                                                                                                                                   	2020-03-13
1	Computer                                                                                                                                                                                                	2020-03-13
30	Hope                                                                                                                                                                                                    	2020-01-01
32	Hope11                                                                                                                                                                                                  	2020-01-01
5	Computer                                                                                                                                                                                                	2020-03-13
6	Computer                                                                                                                                                                                                	2020-03-13
7	Computer yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy                                                                                                                                                               	2020-03-13
8	Computer yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy                                                                                                                                                               	2020-03-13
9	Computer yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy                                                                                                                                                               	2020-03-13
10	Computer yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy                                                                                                                                                               	2020-03-13
11	Computer yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy                                                                                                                                                               	2020-03-13
12	Computer                                                                                                                                                                                                	2020-03-13
13	Computer11                                                                                                                                                                                              	2020-03-13
14	Computer11                                                                                                                                                                                              	2020-03-13
15	Computer11                                                                                                                                                                                              	2020-03-13
16	Computer11                                                                                                                                                                                              	2020-03-13
17	Computer11                                                                                                                                                                                              	2020-03-13
18	Computer11                                                                                                                                                                                              	2020-03-13
19	Computer11                                                                                                                                                                                              	2020-03-13
20	Computer11                                                                                                                                                                                              	2020-03-13
21	Computer2                                                                                                                                                                                               	2020-03-13
22	Computer2                                                                                                                                                                                               	2020-03-13
23	Computer2                                                                                                                                                                                               	2020-03-13
2	Computer2                                                                                                                                                                                               	2020-03-13
24	Antomy                                                                                                                                                                                                  	2020-01-13
25	Book22                                                                                                                                                                                                  	2010-03-13
26	Book22w                                                                                                                                                                                                 	2020-03-22
27	Hope                                                                                                                                                                                                    	2020-01-01
28	Hope                                                                                                                                                                                                    	2020-01-01
29	Hope                                                                                                                                                                                                    	2020-01-01
\.


--
-- Data for Name: category; Type: TABLE DATA; Schema: public; Owner: fareeda
--

COPY public.category (id, name) FROM stdin;
1	History
2	Art
\.


--
-- Name: author_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.author_id_seq', 6, true);


--
-- Name: book_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.book_id_seq', 32, true);


--
-- Name: category_id_seq; Type: SEQUENCE SET; Schema: public; Owner: fareeda
--

SELECT pg_catalog.setval('public.category_id_seq', 1, false);


--
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: fareeda
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- Name: author author_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.author
    ADD CONSTRAINT author_pkey PRIMARY KEY (id);


--
-- Name: book book_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.book
    ADD CONSTRAINT book_pkey PRIMARY KEY (id);


--
-- Name: category category_pkey; Type: CONSTRAINT; Schema: public; Owner: fareeda
--

ALTER TABLE ONLY public.category
    ADD CONSTRAINT category_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--

