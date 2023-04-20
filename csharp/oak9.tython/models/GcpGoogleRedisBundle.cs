// <auto-generated>
//     Generated by the protocol buffer compiler.  DO NOT EDIT!
//     source: gcp/gcp_google_redis_bundle.proto
// </auto-generated>
#pragma warning disable 1591, 0612, 3021, 8981
#region Designer generated code

using pb = global::Google.Protobuf;
using pbc = global::Google.Protobuf.Collections;
using pbr = global::Google.Protobuf.Reflection;
using scg = global::System.Collections.Generic;
namespace Oak9.Tython.Gcp.GoogleRedisBundle {

  /// <summary>Holder for reflection information generated from gcp/gcp_google_redis_bundle.proto</summary>
  public static partial class GcpGoogleRedisBundleReflection {

    #region Descriptor
    /// <summary>File descriptor for gcp/gcp_google_redis_bundle.proto</summary>
    public static pbr::FileDescriptor Descriptor {
      get { return descriptor; }
    }
    private static pbr::FileDescriptor descriptor;

    static GcpGoogleRedisBundleReflection() {
      byte[] descriptorData = global::System.Convert.FromBase64String(
          string.Concat(
            "CiFnY3AvZ2NwX2dvb2dsZV9yZWRpc19idW5kbGUucHJvdG8SI29hazkudHl0",
            "aG9uLmdjcC5nb29nbGVfcmVkaXNfYnVuZGxlGhNzaGFyZWQvc2hhcmVkLnBy",
            "b3RvGhNnY3AvZ2NwX3JlZGlzLnByb3RvIksKC0dvb2dsZVJlZGlzEjwKDnJl",
            "ZGlzX2luc3RhbmNlGAEgASgLMiQub2FrOS50eXRob24uZ2NwLnJlZGlzLlJl",
            "ZGlzSW5zdGFuY2ViBnByb3RvMw=="));
      descriptor = pbr::FileDescriptor.FromGeneratedCode(descriptorData,
          new pbr::FileDescriptor[] { global::Oak9.Tython.Shared.SharedReflection.Descriptor, global::Oak9.Tython.Gcp.Redis.GcpRedisReflection.Descriptor, },
          new pbr::GeneratedClrTypeInfo(null, null, new pbr::GeneratedClrTypeInfo[] {
            new pbr::GeneratedClrTypeInfo(typeof(global::Oak9.Tython.Gcp.GoogleRedisBundle.GoogleRedis), global::Oak9.Tython.Gcp.GoogleRedisBundle.GoogleRedis.Parser, new[]{ "RedisInstance" }, null, null, null, null)
          }));
    }
    #endregion

  }
  #region Messages
  public sealed partial class GoogleRedis : pb::IMessage<GoogleRedis>
  #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
      , pb::IBufferMessage
  #endif
  {
    private static readonly pb::MessageParser<GoogleRedis> _parser = new pb::MessageParser<GoogleRedis>(() => new GoogleRedis());
    private pb::UnknownFieldSet _unknownFields;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public static pb::MessageParser<GoogleRedis> Parser { get { return _parser; } }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public static pbr::MessageDescriptor Descriptor {
      get { return global::Oak9.Tython.Gcp.GoogleRedisBundle.GcpGoogleRedisBundleReflection.Descriptor.MessageTypes[0]; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    pbr::MessageDescriptor pb::IMessage.Descriptor {
      get { return Descriptor; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public GoogleRedis() {
      OnConstruction();
    }

    partial void OnConstruction();

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public GoogleRedis(GoogleRedis other) : this() {
      redisInstance_ = other.redisInstance_ != null ? other.redisInstance_.Clone() : null;
      _unknownFields = pb::UnknownFieldSet.Clone(other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public GoogleRedis Clone() {
      return new GoogleRedis(this);
    }

    /// <summary>Field number for the "redis_instance" field.</summary>
    public const int RedisInstanceFieldNumber = 1;
    private global::Oak9.Tython.Gcp.Redis.RedisInstance redisInstance_;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public global::Oak9.Tython.Gcp.Redis.RedisInstance RedisInstance {
      get { return redisInstance_; }
      set {
        redisInstance_ = value;
      }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public override bool Equals(object other) {
      return Equals(other as GoogleRedis);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public bool Equals(GoogleRedis other) {
      if (ReferenceEquals(other, null)) {
        return false;
      }
      if (ReferenceEquals(other, this)) {
        return true;
      }
      if (!object.Equals(RedisInstance, other.RedisInstance)) return false;
      return Equals(_unknownFields, other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public override int GetHashCode() {
      int hash = 1;
      if (redisInstance_ != null) hash ^= RedisInstance.GetHashCode();
      if (_unknownFields != null) {
        hash ^= _unknownFields.GetHashCode();
      }
      return hash;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public override string ToString() {
      return pb::JsonFormatter.ToDiagnosticString(this);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public void WriteTo(pb::CodedOutputStream output) {
    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
      output.WriteRawMessage(this);
    #else
      if (redisInstance_ != null) {
        output.WriteRawTag(10);
        output.WriteMessage(RedisInstance);
      }
      if (_unknownFields != null) {
        _unknownFields.WriteTo(output);
      }
    #endif
    }

    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    void pb::IBufferMessage.InternalWriteTo(ref pb::WriteContext output) {
      if (redisInstance_ != null) {
        output.WriteRawTag(10);
        output.WriteMessage(RedisInstance);
      }
      if (_unknownFields != null) {
        _unknownFields.WriteTo(ref output);
      }
    }
    #endif

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public int CalculateSize() {
      int size = 0;
      if (redisInstance_ != null) {
        size += 1 + pb::CodedOutputStream.ComputeMessageSize(RedisInstance);
      }
      if (_unknownFields != null) {
        size += _unknownFields.CalculateSize();
      }
      return size;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public void MergeFrom(GoogleRedis other) {
      if (other == null) {
        return;
      }
      if (other.redisInstance_ != null) {
        if (redisInstance_ == null) {
          RedisInstance = new global::Oak9.Tython.Gcp.Redis.RedisInstance();
        }
        RedisInstance.MergeFrom(other.RedisInstance);
      }
      _unknownFields = pb::UnknownFieldSet.MergeFrom(_unknownFields, other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public void MergeFrom(pb::CodedInputStream input) {
    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
      input.ReadRawMessage(this);
    #else
      uint tag;
      while ((tag = input.ReadTag()) != 0) {
        switch(tag) {
          default:
            _unknownFields = pb::UnknownFieldSet.MergeFieldFrom(_unknownFields, input);
            break;
          case 10: {
            if (redisInstance_ == null) {
              RedisInstance = new global::Oak9.Tython.Gcp.Redis.RedisInstance();
            }
            input.ReadMessage(RedisInstance);
            break;
          }
        }
      }
    #endif
    }

    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    void pb::IBufferMessage.InternalMergeFrom(ref pb::ParseContext input) {
      uint tag;
      while ((tag = input.ReadTag()) != 0) {
        switch(tag) {
          default:
            _unknownFields = pb::UnknownFieldSet.MergeFieldFrom(_unknownFields, ref input);
            break;
          case 10: {
            if (redisInstance_ == null) {
              RedisInstance = new global::Oak9.Tython.Gcp.Redis.RedisInstance();
            }
            input.ReadMessage(RedisInstance);
            break;
          }
        }
      }
    }
    #endif

  }

  #endregion

}

#endregion Designer generated code