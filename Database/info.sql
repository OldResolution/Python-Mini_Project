PGDMP  4    1                |         	   PyProject    16.2    16.2 	    �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    16397 	   PyProject    DATABASE     �   CREATE DATABASE "PyProject" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'English_United States.1252';
    DROP DATABASE "PyProject";
                postgres    false            �            1259    24656    info    TABLE     �   CREATE TABLE public.info (
    user_id integer NOT NULL,
    user_name text NOT NULL,
    user_password text NOT NULL,
    user_emailid text NOT NULL
);
    DROP TABLE public.info;
       public         heap    postgres    false            �            1259    24661    info_user_id_seq    SEQUENCE     �   ALTER TABLE public.info ALTER COLUMN user_id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.info_user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);
            public          postgres    false    219            �          0    24656    info 
   TABLE DATA           O   COPY public.info (user_id, user_name, user_password, user_emailid) FROM stdin;
    public          postgres    false    219   �       �           0    0    info_user_id_seq    SEQUENCE SET     >   SELECT pg_catalog.setval('public.info_user_id_seq', 3, true);
          public          postgres    false    220            X           2606    24663    info UserInfo_pkey 
   CONSTRAINT     W   ALTER TABLE ONLY public.info
    ADD CONSTRAINT "UserInfo_pkey" PRIMARY KEY (user_id);
 >   ALTER TABLE ONLY public.info DROP CONSTRAINT "UserInfo_pkey";
       public            postgres    false    219            �   ?   x�3�,(J,KM��442615�q����8��2�8--��LA�b#3��������\�=... \�$     