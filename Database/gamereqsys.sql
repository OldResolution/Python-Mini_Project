PGDMP  #    %                |            gamereq    16.2    16.2     �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    16396    gamereq    DATABASE     z   CREATE DATABASE gamereq WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'English_India.1252';
    DROP DATABASE gamereq;
                postgres    false            �            1259    16398    game_requirements    TABLE       CREATE TABLE public.game_requirements (
    id integer NOT NULL,
    game_title character varying(500) NOT NULL,
    minimum_os_version character varying(500),
    recommended_os_version character varying(500),
    minimum_processor character varying(500),
    recommended_processor character varying(500),
    minimum_memory character varying(500),
    recommended_memory character varying(500),
    minimum_graphics character varying(500),
    recommended_graphics character varying(500),
    storage_space character varying(500)
);
 %   DROP TABLE public.game_requirements;
       public         heap    postgres    false            �            1259    16397    game_requirements_id_seq    SEQUENCE     �   CREATE SEQUENCE public.game_requirements_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 /   DROP SEQUENCE public.game_requirements_id_seq;
       public          postgres    false    216            �           0    0    game_requirements_id_seq    SEQUENCE OWNED BY     U   ALTER SEQUENCE public.game_requirements_id_seq OWNED BY public.game_requirements.id;
          public          postgres    false    215            �            1259    16407    sys_components    TABLE     ]  CREATE TABLE public.sys_components (
    component_id integer NOT NULL,
    component_name character varying(255),
    component_type character varying(4),
    component_rating integer,
    CONSTRAINT sys_components_component_type_check CHECK (((component_type)::text = ANY ((ARRAY['CPU'::character varying, 'GPU'::character varying])::text[])))
);
 "   DROP TABLE public.sys_components;
       public         heap    postgres    false            �            1259    16406    sys_components_component_id_seq    SEQUENCE     �   CREATE SEQUENCE public.sys_components_component_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 6   DROP SEQUENCE public.sys_components_component_id_seq;
       public          postgres    false    218            �           0    0    sys_components_component_id_seq    SEQUENCE OWNED BY     c   ALTER SEQUENCE public.sys_components_component_id_seq OWNED BY public.sys_components.component_id;
          public          postgres    false    217            U           2604    16401    game_requirements id    DEFAULT     |   ALTER TABLE ONLY public.game_requirements ALTER COLUMN id SET DEFAULT nextval('public.game_requirements_id_seq'::regclass);
 C   ALTER TABLE public.game_requirements ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    215    216    216            V           2604    16410    sys_components component_id    DEFAULT     �   ALTER TABLE ONLY public.sys_components ALTER COLUMN component_id SET DEFAULT nextval('public.sys_components_component_id_seq'::regclass);
 J   ALTER TABLE public.sys_components ALTER COLUMN component_id DROP DEFAULT;
       public          postgres    false    218    217    218            �          0    16398    game_requirements 
   TABLE DATA           �   COPY public.game_requirements (id, game_title, minimum_os_version, recommended_os_version, minimum_processor, recommended_processor, minimum_memory, recommended_memory, minimum_graphics, recommended_graphics, storage_space) FROM stdin;
    public          postgres    false    216   �       �          0    16407    sys_components 
   TABLE DATA           h   COPY public.sys_components (component_id, component_name, component_type, component_rating) FROM stdin;
    public          postgres    false    218   ~+       �           0    0    game_requirements_id_seq    SEQUENCE SET     G   SELECT pg_catalog.setval('public.game_requirements_id_seq', 88, true);
          public          postgres    false    215            �           0    0    sys_components_component_id_seq    SEQUENCE SET     N   SELECT pg_catalog.setval('public.sys_components_component_id_seq', 72, true);
          public          postgres    false    217            Y           2606    16405 (   game_requirements game_requirements_pkey 
   CONSTRAINT     f   ALTER TABLE ONLY public.game_requirements
    ADD CONSTRAINT game_requirements_pkey PRIMARY KEY (id);
 R   ALTER TABLE ONLY public.game_requirements DROP CONSTRAINT game_requirements_pkey;
       public            postgres    false    216            [           2606    16413 "   sys_components sys_components_pkey 
   CONSTRAINT     j   ALTER TABLE ONLY public.sys_components
    ADD CONSTRAINT sys_components_pkey PRIMARY KEY (component_id);
 L   ALTER TABLE ONLY public.sys_components DROP CONSTRAINT sys_components_pkey;
       public            postgres    false    218            �      x��<�r۸�k�+P��,�M*�i۲W�_�qT�fCK�ŊD꒔g5�08_2�  	� %'鞪���8 �������8��(^&�3��&�Q^z1r��\$iHL��}�$��?]W��������W2"g7r��dKƾ�ө��6Ma�%)���tq��!���Z��ĥz6�!��5�>������Sl:�g4�L�5��p=�>�æ��Ę�s�b��:��&s�k ?C~�lz?'�10�`@�Lx���]�<��n"��y5ʝ>ʔ�#5$O-��� �O12������z1���k�X��O��)�:��tҽ{�N,�{,�$&wstU�7t@�U8c]���l691L�.\�IL���.�`��z�MG�G7q��w� 5?��'��dLLF�N�G2� �Ɨ9H���β,Ȳ(���\�!��!ج��&1�1��ʱ:l^=�1�0�p=�>�#�ĸZ�����/���+8�L��d��A���'7�_I�Q�bgy�,`�[`� g�b�n�x7�d�9W�
R��1J\����r��G��rt~K�8�a�G�-���.4�,_o�Xznc��T�YT��L�%7�|�?`do��$J�E,�d�lw�(�s��u���"H��x��6E�+5E��,�����ʨ���N��Zw�}Ҙ675�H��+�����s�a;f�8<����ᗨYLF�uv�6{)(��e"XG.�NK�{6�<Lu\�!G켾����j��0%7�ֶ��Ư��5���0$�~�K�������f�fM.�sI�%J�qI7[��[�,>���C�iߎ���a�+�@X�����$�����X!��P�Q�h��ֽ�ۉ��J#������
��e0t1c}���a�#��r�S/����n(~�<y��mF�x��A�#�Ĥ�6$Z�g�J"���G�����cө���h�+^Ju�zP�r1 2|*)�.��Jލ��!�z��rV%+ݣ]��G�~<�DjY@�y��;�*o��o)Lq����K���߫&��G���35x�5 o�4���J��w��9e8���7�gc�x��8u�V�q��O�a�0��AӒ���?��X�|Rw�������w�s����S9"B�!��Ϻ�E<[���5U|�`��0�[B&ٸ�٬ΰP-�3��z�a�8��6$ԁ�7���ȑbwD��w�P)��#�����C\N*q�"�?N��E`�D��0v�'�����&�Hir=Et;�黕6��l�w�� �Q"k�^<A�n�
�ؘTPyTT��z[LT�E�$!���~��-`Q3�G<o'���I9/xG&�6C�����}H��#|
�e&`��i��we٧ǣQ�#�lvi�(��t��Մ,̫��mV�����qh��.x܄b~ ���u��HbT���M�e�0v��~`����N�	�	D=��y�m�QC�8�Ê^#T�F��%֩e�Ne4m�n�@���"T� ���+(@�[j?�Ω]9�.���}��k�7���w��a/��,O�O�2�$����_��8��C!������C���� k���">�2�S� ����@*�{��b��r�@x>���f/I�N��%>�4�f�A�xR�:@V z}�Mq����^�d�2��`���N�2�L���&|[fO�Gt|��6d��.%�b;We�C��J�llq�<D]`a���QX�:-
$�<s'��M�<+��מ��0]��]�� �ӄ�V�ۧY��R�xѻ��:f�3��sl̂s&[���)��n��0����X�<�|>���ˬ��|���@�-Bj��������B1�Q�u�9PKųY����K�G��w�_n�l�r��}�[���n�둌�zY�w �֒5n�o����0F�>e^H�n����u�k�'��0`uG�I��|��r�*�`/�$�N�N4�����v~��B��Q!<Tܭ�<���z��a�ƬŅ6�Q��oW��[�P�d���Г���R�bjg���Dq�H���ڨ���ڴC.C��������ĀB���=�,V0�S�/�PU����S�Q��ϢA\��������)���H��4
3�{@��P�����0��A�-����I�}!f��~Yl�x�{�M�XG;�3�-�v��M@��@㐧`t��vـ2$�1�^E�0;����.�Rf��i�H��Я��Cg���<Z>�v��!��.��ףW䟚I�2l���Ӭ�>yCːiL>�*���L��k�櫏\���cNUvI�:�O,Ĵ9%�<ze��C�Q^'��i��-���������plC���k�
�J�l��P:��]�r=ˊ%��G �8LQL�(�`�	�3\ y �V�~*�X��vn�p�i�|=����6�ަL�+b���fFl��zL5i��:���-m[֜��ׯG��aӷȆې�F@x	��%nH
+t�N���1n���W�1����R����d*��db�J4:[>�"\��N(�]��>�H����&V&�UgĔ��Z:�������;�i�Md��b����GU�HAQ�m[����JO"�t�dy�:"5߀Jx��/u�̤��j���������޿���Q֩I�N:y.��;�Ug��6�VW
���W@�ek����*8��ě�T��E+\���r�=n�IV](�!T�#�!�h���]�[�wT]zRբx�x�f�Ѩ ���B�����V+�nrӕ�H�,�$l��Bё%�����]Km��*$�:����9$Au�����zb�4�6
7Hb��������O��-!?j�h�(�*)\��6�!���5����|y�9��)Lm�,�@tLBuGLBG�e��ڒi�4��GI�s�W�M���%bf�~n�i����o��:��ulE�o^��}F	��Ԅ0�85B�?�vA
V�1��M&n]��`�5��	�Y��cj��0n0�%�o|������c*\�s��S �Z܍�?�֬g���b=�a)5�V����@}T>Wbс���ׯۇs��Iu�m��w�l���4��N	��f����O�ѐ��c�W4#Ktc�L��X��v @�h r��L'u�/}�[ V�21k�wN+�;1b+7�#�)�v�'���;��0��Cq�A����C*�����ܰt1��Vո�����ED�R��"yS9� >�fa��;n1�5q��40:�̛Z���p�;���x��xE����?�O�΋?���%�j,-=���.sh)Z6p��g�h��l�A��T3��~GD%���܎�M��YVŖ�paD�E�$������wC�p�'�f���|h66�9�����3X�F�4���u�\9g�2*h�˅Ӑ��INn�i��r9�c��j0���)8��ʦ�XV��Bb�W��RA�0����� �o�a��Py��F�u�m��~��=[��Ȕ�����*�D:_
=7m�QLE�IqA�9���ܙ��]�~[<a�M	 ��+�ԄdR ��;�/*Z��-�a|��`bJ�b-SY��m�ؤ��ܫ������L̡� ����:�'��~-o�C�!��{��g������mW�V��ћ��=e��E�V�
[�;�P�������%�d<�v�;�8�F�
2T��Tzk4�Q\�T�E�o�>�9��$%�U�]K��AËޚ��������JvTM�k��}��*_2.�n���ā�Y(�k�]�Uϔ���J�UfM�^XdеY<v唐r��7��1P�@�/Q�T�(T]%�je��U,S���V�Vq�L�v؂T,#�''�`�^т!��W40E)o���۩�7��<�i�M��|Ɠ�|9�2+o)l�cgJ��Ny�ԵN�A���a��} ݅P�)�d�^j�g�M�\�*-��]���{���D����Jn1��9��_/����W�FUO�%�l��޲a�c]�o���)j;��v֭�5�g1t��x7So�M�͉��潛�6�VI�+T��ѵ,z#� �  &=K;[&���m2��*��W� ��P*6�9w��\��)`�_����su���i�FQ:��z�`-�  4�NV��U[�L��	^y���y�8���hC/���.���v�A�~e�6���e��AдJ1���RT��>em�"�l6���a��'�����4��d��QŅ���ւpgK1�SP�j�ku9N�>\6k�{l�EzJ�p�l������kݽ�\�_�|	J�'�hoJ�й-���S�?��l����jaSvHR�ݒz����d�hT�R�x{pq��qʽk�����LY2�����i#�E�`�� �!��䙾`�	�5ɀ�@c�1OȀ���4��<��ɮ�]IO$v���o���E�u��2�<~�v���;���&O��.i�v��c��
�(�z�XaP�;g����솰���D@v��%���˘��;Nv��DY%9�a;7�D�z��gyJ��C� -@�Ϙ��dɦޚ��xktj,�q�z
�+�1���N"r��!eKᄨZ��Gn�7
Ɠ0��b�����(��Q��1@vEW�d�&SݰV�ݿ�d�d}S������o-���mtzw'ߐ���<)>�+W.����p[�[ݸKDo�Ϻ��}�:���N�"���	�~�SwL1>S4"1ѓ	$ޔ&���3���E/؁|��	^�B�Q�SN|��c>q�B��@'����[i���� ���=�͒�׆�k�E�~����8�^q�&��-�Cn�	�L��lz����ē\���
�L# 6^YbG1�t�.�"X�C|]���}BV@���G1-"G0}/���e<��n���gw��=�;�e�"�_H<�Du��]EO� Ҙ0���s�HS`8���Å�+~N|W;����Y%�x�K���ݹ96Ɩ��QF��ŋ��'�XӪ@�������!7�c�kD�_�!t��*E��ޒ����%� �T��ǂ����!����t����f�&Z~L�Ob�4h���!khQ5/����')\��.�4�V^�QcQ*W����1A�H��Q�S��Y~w��SyX���՞2�r��l��Xw̙-��<��-}� ���'�/�@Ó�18-�[���28+�#t��^X`.�Y|�"7����s ֲ��3S(MK$�,>�#�������/��m      �   _  x�u�Mn1���)t���e�nP�H�i�E7:@��&�����4��[|�ӣFV����w�7b;섒N���?VFJ��=�!S����0ۏ�-��C��v�<֡zT�:zNC
C���#��>%����3�\+�3���<^Zk�x��H�{6S�hex�dړ��l��v���\���r�l���H����t��9����R-9��D���3�5�1K#I٭�SWC2v����v��"�ͯ�b �"��W�)����� J�"���W$�y?A�֘���]N�#j{5��r�CϡpZ��a㟗�xVr�?S����؝g���%�Ͷ������"nO�Q�FIl|[�"�z�*'��.<?G�q��[�m�U����\�\�P�ZX����5�-��/P��F��@�Z��� ���n��T+����OG�i����6���0��ެn�����Qa��A����2�H݂n��0jkc@�g�	�-�����S�A�P�Z��>�~nŨk������B]��4T���2�|q��-�� N[gr5�*
�*,�1ي�&F[^v����<���eL/������
�}��z�/�����z�O+�d     