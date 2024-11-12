-- SEQUENCE: public.locations_id_seq

-- DROP SEQUENCE IF EXISTS public.locations_id_seq;

CREATE SEQUENCE IF NOT EXISTS public.locations_id_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 9223372036854775807
    CACHE 1;

ALTER SEQUENCE public.locations_id_seq
    OWNER TO "kiffin.tse";





-- SEQUENCE: public.registers_id_seq

-- DROP SEQUENCE IF EXISTS public.registers_id_seq;

CREATE SEQUENCE IF NOT EXISTS public.registers_id_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 9223372036854775807
    CACHE 1;

ALTER SEQUENCE public.registers_id_seq
    OWNER TO "kiffin.tse";





-- SEQUENCE: public.can_labtest_uploads_id_seq

-- DROP SEQUENCE IF EXISTS public.can_labtest_uploads_id_seq;

CREATE SEQUENCE IF NOT EXISTS public.can_labtest_uploads_id_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 9223372036854775807
    CACHE 1;

ALTER SEQUENCE public.can_labtest_uploads_id_seq
    OWNER TO "kiffin.tse";



-- SEQUENCE: public.action_tip_translations_id_seq

-- DROP SEQUENCE IF EXISTS public.action_tip_translations_id_seq;

CREATE SEQUENCE IF NOT EXISTS public.action_tip_translations_id_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 9223372036854775807
    CACHE 1;

ALTER SEQUENCE public.action_tip_translations_id_seq
    OWNED BY public.action_tip_translations.id;

ALTER SEQUENCE public.action_tip_translations_id_seq
    OWNER TO "kiffin.tse";




-- SEQUENCE: public.action_tips_id_seq

-- DROP SEQUENCE IF EXISTS public.action_tips_id_seq;

CREATE SEQUENCE IF NOT EXISTS public.action_tips_id_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 9223372036854775807
    CACHE 1;

ALTER SEQUENCE public.action_tips_id_seq
    OWNED BY public.action_tips.id;

ALTER SEQUENCE public.action_tips_id_seq
    OWNER TO "kiffin.tse";