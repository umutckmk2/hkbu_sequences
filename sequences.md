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